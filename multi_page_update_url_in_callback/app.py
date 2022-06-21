"""
Example of updating url in a callback.  Note that the dcc.Location must be in app.py
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
    [navbar, dash.page_container, dcc.Location(id="url", refresh=True)],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
