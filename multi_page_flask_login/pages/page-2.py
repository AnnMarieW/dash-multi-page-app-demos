import dash
from dash import html, dcc, Output, Input, callback
from pages.login import layout as login
from flask_login import current_user

dash.register_page(__name__)

layout = html.Div(id="page-2-auth-content")

logged_in_layout = html.Div(
    [
        html.H1("Page 2"),
        dcc.RadioItems(
            id="page-2-radios",
            options=[{"label": i, "value": i} for i in ["Orange", "Blue", "Red"]],
            value="Orange",
        ),
        html.Div(id="page-2-content"),
        html.Br(),
        dcc.Link("Go to Page 1", href="/page-1"),
        html.Br(),
        dcc.Link("Go back to home", href="/"),
    ]
)


@callback(Output("page-2-auth-content", "children"), Input("url", "href"))
def authenticate(_):
    if current_user.is_authenticated:
        return logged_in_layout
    return login


@callback(Output("page-2-content", "children"), Input("page-2-radios", "value"))
def page_2_radios(value):
    return f'You have selected "{value}"'
