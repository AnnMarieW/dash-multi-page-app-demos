"""
This is a minimal example of changing themes with the ThemeSwitchAIO component
Note - this requires dash-bootstrap-components>=1.0.0 and dash>=2.5.1 dash-bootstrap-templates>=1.0.4.

See more information at https://hellodash.pythonanywhere.com/

"""

from dash import Dash, page_registry, page_container
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

# select the Bootstrap stylesheets and figure templates for the theme toggle here:
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY
theme_toggle = ThemeSwitchAIO(
    aio_id="theme",
    themes=[url_theme2, url_theme1],
    icons={"left": "fa fa-sun", "right": "fa fa-moon"},
)

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme2, dbc_css])


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
    [navbar, theme_toggle, page_container], fluid=True, className="dbc"
)

if __name__ == "__main__":
    app.run_server(debug=True)
