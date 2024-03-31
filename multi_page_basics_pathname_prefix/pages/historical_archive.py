from dash import html, dcc, callback, Input, Output

import dash

dash.register_page(__name__)


def layout(**kwargs):
    return html.H1("Historical Archive")
