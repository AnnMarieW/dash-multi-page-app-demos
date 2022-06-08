import uuid
from dash import Dash, html, dcc
import dash


## Diskcache
import diskcache

cache_lc = diskcache.Cache("./cache_lc")


external_stylesheets = [
    # Dash CSS
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    # Loading screen CSS
    "https://codepen.io/chriddyp/pen/brPBPO.css",
]

session_id = str(uuid.uuid4())

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Store(data=session_id, id="session-id"),
        html.H1("Multi-page cache examples"),
        html.Div(
            [
                html.Div(dcc.Link(f"{page['name']}", href=page["path"]))
                for page in dash.page_registry.values()
            ]
        ),
        html.Hr(),
        dcc.Markdown(
            """
            For more information, see dash tutorial Sharing Data Between Callbacks chapter
              - [Example 3 Caching and Signaling](https://dash.plotly.com/sharing-data-between-callbacks#example-3---caching-and-signaling)
              - [Example 4 User Based Session Data on the server](https://dash.plotly.com/sharing-data-between-callbacks#example-4---user-based-session-data-on-the-server)

            """,
            style={"margin": 20},
        ),
        dash.page_container,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True, processes=6, threaded=False)
