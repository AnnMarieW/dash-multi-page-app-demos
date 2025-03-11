"""
Example of updating url in a callback in dash>=2.9.0.

"""


import dash
from dash import dcc
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    [
        dbc.Button("Home", href="/", color="secondary", className="me-1"),
        dbc.Button("Stock Analysis", href="/stocks/AAPL", color="secondary"),
    ],
    brand="Multi Page App Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [
        dcc.Location(id="url", refresh="callback-nav"),
        navbar, dash.page_container
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
