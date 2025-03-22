"""
Navigation in a callback.

With Dash Pages, the routing callback is under the hood, which reduces the amount of boilerplate code you need to write.
The best way to navigate is to use components such as the `dcc.Link` or `dbc.Button`. When the
 user clicks on these links, it will navigate to the new page without refreshing the page making the navigation
very fast -- and the best part:  No callback required!.

This works well when you have predefined links. However, at times, you may want to navigate based on an input field,
dropdown, or clicking on a figure etc.  In these cases, you can update `href` prop of a `dcc.Location` in a callback.
Prior to dash 2.9.2, this was not recommended because it will refresh the page.

** NEW in dash>=2.9.2 **

It is now possible to navigate to the new page without refreshing the page.  Set `refresh="callback-nav"`

dcc.Location(id="url", refresh="callback-nav")


This example updates the URL in a callback when the user clicks on a figure.
"""

from dash import Dash, dcc, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    dbc.Button("Home", href="/", color="secondary", className="me-1"),
    brand="Multi Page App Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh="callback-nav"),
        navbar, page_container,
    ], fluid=True
)

if __name__ == "__main__":
    app.run(debug=True)
