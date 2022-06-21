"""
Note that the callback will trigger even if prevent_initial_call=True. This is because dcc.Location must
be in app.py.  Since the dcc.Location comonent is not in the layout when navigating to this page, it triggers the callback.
The workaround is to check if the input value is None.

"""


import dash
from dash import html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")


layout = html.Div(
    [
        dbc.Input(
            id="ticker-search",
            placeholder="Search ticker or company name...",
            className="my-4",
            debounce=True,
        ),
    ]
)


@callback(
    Output("url", "href"), Input("ticker-search", "value"), prevent_initial_call=True
)
def search(ticker):
    if ticker is None or ticker == "":
        return dash.no_update
    return f"/stocks/{ticker}"
