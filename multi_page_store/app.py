"""
This example demonstrates sharing data between pages of a multi-page app.
Note that dcc.Store is in the app.py file so that it's accessible to all pages.
"""


from dash import html, dcc
import dash

app = dash.Dash(__name__, use_pages=True)

app.layout = html.Div(
    [
        dcc.Store(id="store", data={}),
        html.H1("Multi Page App Demo: Sharing data between pages"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']}", href=page["path"]),
                )
                for page in dash.page_registry.values()
            ]
        ),
        html.Hr(),
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
