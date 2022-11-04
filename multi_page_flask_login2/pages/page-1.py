import dash
from dash import html, dcc, Output, Input, callback

dash.register_page(__name__)


layout = html.Div(
    [
        html.H1("Page 1"),
        dcc.Dropdown(
            id="page-1-dropdown",
            options=[{"label": i, "value": i} for i in ["LA", "NYC", "MTL"]],
            value="LA",
        ),
        html.Div(id="page-1-content"),
        html.Br(),
        dcc.Link("Go to Page 2", href="/page-2"),
        html.Br(),
        dcc.Link("Go back to home", href="/"),
    ]
)


@callback(Output("page-1-content", "children"), Input("page-1-dropdown", "value"))
def page_1_dropdown(value):
    return f'You have selected "{value}"'
