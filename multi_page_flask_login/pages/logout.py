import dash
from dash import html, dcc

dash.register_page(__name__)


layout = html.Div(
    [
        html.Div(html.H2("You have been logged out - Please login")),
        html.Br(),
        dcc.Link("Home", href="/"),
    ]
)
