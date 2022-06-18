import dash
from dash import html, dcc


dash.register_page(__name__)

# Login screen
layout = html.Div(
    [
        html.H2("Please log in to continue:", id="h1"),
        dcc.Input(placeholder="Enter your username", type="text", id="uname-box"),
        dcc.Input(placeholder="Enter your password", type="password", id="pwd-box"),
        html.Button(children="Login", n_clicks=0, type="submit", id="login-button"),
        html.Div(children="", id="output-state"),
        html.Br(),
        dcc.Link("Home", href="/"),
    ]
)
