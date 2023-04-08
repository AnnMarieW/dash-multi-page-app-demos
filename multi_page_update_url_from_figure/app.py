"""
Navigation in a callback.

With Dash Pages, the routing callback is under the hood, which reduces the amount of boilderplate code you need to write.
The best way to navigate is for the user to click on a link made with components such as the `dcc.Link` or `dbc.Button`.
 It navigates to the new page without refreshing the page making the navigation very fast -- and the best part:  No callback required!.

This works well when you have predefined links. However, at times, you may want to navigate based on an input field,
dropdown, or clicking on a figure etc.  Rather than updating the `href` prop of a `dcc.Location` in a callback,
 it's a best practice to update the `dcc.Link` in a callback.  This makes it so that the user can click on the new
 link to navigate to a different page.

In this example, when the user clicks on an airport in the figure, we display a card with links to get more
 information on that airport.

To see more examples, including an

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
