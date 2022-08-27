"""
Navigation in a callback.

With Dash Pages, the routing callback is under the hood, which reduces the amount of boilderplate code you need to write.
The best way to navigate is to use components such as the `dcc.Link` or `dbc.Button`. When the
 user clicks on these links, it will navigate to the new page without refreshing the page making the navigation
very fast -- and the best part:  No callback required!.

This works well when you have predefined links. However, at times, you may want to navigate based on an input field,
dropdown, or clicking on a figure etc.  In these cases, you can update the link dynamically in a callback.

While it's possible to update the `href` prop of a `dcc.Location` in a callback, this is not recommended because it
 refreshes the page.

This example updates a link in a callback when the user clicks on a figure.
"""

import dash

import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    [
        dbc.Button("Airports", href="/", color="secondary", className="me-1"),
    ],
    brand="Multi Page App Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, dash.page_container],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
