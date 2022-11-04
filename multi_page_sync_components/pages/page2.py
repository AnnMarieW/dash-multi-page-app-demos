from dash import dcc, html
from dash import Output, Input, State, callback

import dash
import utils

dash.register_page(__name__, path="/page2")

layout = html.Div(
    [
        html.Label("Page 2 Select Year"),
        utils.app_spanning_input,
        html.Div(id="page2-out"),
    ]
)

@callback(
    Output("page2-out", "children"),
    Input("all-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"