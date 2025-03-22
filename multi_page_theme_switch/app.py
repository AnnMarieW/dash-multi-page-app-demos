"""
This is a minimal example of changing themes with Bootstrap color modes
See more information at https://hellodash.pythonanywhere.com/adding-themes/color-modes

"""

from dash import Dash, html, page_registry, page_container, clientside_callback, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# adds  templates to plotly.io
load_figure_template(["flatly", "flatly_dark"])


color_mode_switch =  html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch( id="switch", value=True, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.FLATLY, dbc_css])


navbar = dbc.NavbarSimple(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(page["name"], href=page["path"])
                for page in page_registry.values()
                if page["module"] != "pages.not_found_404"
            ],
            nav=True,
            label="More Pages",
        ),
    ],
    brand="Multi Page App Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, color_mode_switch, page_container], fluid=True, className="dbc"
)

clientside_callback(
    """ 
    (switchOn) => {
       document.documentElement.setAttribute('data-bs-theme', switchOn ? 'light' : 'dark');  
       return window.dash_clientside.no_update
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)

if __name__ == "__main__":
    app.run(debug=True)
