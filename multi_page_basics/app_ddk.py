import dash
from dash import dcc

import dash_design_kit as ddk

app = dash.Dash(__name__)

app.layout = ddk.App(
    [
        ddk.Header(
            [
                ddk.Menu(dcc.Link(page["name"], href=page["path"]))
                for page in dash.page_registry
            ]
        ),
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
