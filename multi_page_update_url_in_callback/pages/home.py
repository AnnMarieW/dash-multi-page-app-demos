"""
Note that the callback will trigger even if prevent_initial_call=True. This is because dcc.Location must
be in app.py.  Since the dcc.Location component is not in the layout when navigating to this page, it triggers the callback.
The workaround is to check if the input value is None.

"""


import dash
from dash import dcc, html, Input, Output, State, callback, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

intro = """
## Navigation in a callback.

With Dash Pages, the routing callback is under the hood, which reduces the amount of boilderplate code you need to write.
The best way to navigate is to use components such as the `dcc.Link` or `dbc.Button`. When the
 user clicks on these links, it will navigate to the new page without refreshing the page making the navigation
very fast -- and the best part:  No callback required!.

This works well when you have predefined links. However, at times, you may want to navigate based on an input field, 
dropdown, or clicking on a figure etc.  In these cases, you can update the link dynamically in a callback.

While it's possible to update the `href` prop of a `dcc.Location` in a callback, this is not recommended because it
 refreshes the page.  


### Example 1 
Using `dcc.Location` to update the url.  **This is not recommended ** since it refreshes the page.  Note the
 `dcc.Location` must be in `app.py`
"""

example2 = """
### Example 2
"Using `dcc.Link` and `html.Button` to navigate without refreshing the page"
"""

example3 = """
### Example 3
Using `dbc.Button` to navigate without refreshing the page
"""


layout = html.Div(
    [
        dcc.Markdown(intro),
        dbc.Input(
            id="ticker-search1",
            placeholder="Search ticker or company name...",
            className="mb-5",
            debounce=True,
        ),
        dcc.Markdown(example2),
        dcc.Input(
            id="ticker-search2",
            placeholder="Search ticker or company name...",
            className="mb-5",
        ),
        dcc.Link(
            html.Button("submit", n_clicks=0, id="ticker-search2-btn"),
            id="ticker-search2-link",
            href="/",
        ),
        dcc.Markdown(example3),
        dbc.InputGroup(
            [
                dbc.Input(
                    id="ticker-search3",
                    placeholder="Search ticker or company name...",
                    style={"maxWidth": 400},
                ),
                dbc.Button("submit", n_clicks=0, id="ticker-search3-btn", href="/"),
            ]
        ),
    ]
)


@callback(
    Output("url", "href"), Input("ticker-search1", "value"), prevent_initial_call=True
)
def search(ticker):
    if ticker is None or ticker == "":
        return dash.no_update
    return f"/stocks/{ticker}"


@callback(
    Output("ticker-search2-link", "href"),
    Input("ticker-search2", "value"),
    prevent_initial_call=True,
)
def search(ticker):
    if ticker is None or ticker == "":
        return dash.no_update
    return f"/stocks/{ticker}"


@callback(
    Output("ticker-search3-btn", "href"),
    Input("ticker-search3", "value"),
    prevent_initial_call=True,
)
def search(ticker):
    if ticker is None or ticker == "":
        return dash.no_update
    return f"/stocks/{ticker}"
