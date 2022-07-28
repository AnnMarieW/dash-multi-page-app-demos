import dash
from dash import html, dcc
from flask_login import logout_user, current_user

dash.register_page(__name__)


def layout():
    if current_user.is_authenticated:
        logout_user()
    return html.Div(
        [
            html.Div(html.H2("You have been logged out - Please login")),
            html.Br(),
            dcc.Link("Home", href="/"),
        ]
    )
