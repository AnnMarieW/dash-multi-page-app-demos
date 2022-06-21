import dash
import dash_bootstrap_components as dbc
from pages import bar_charts, heatmaps, histograms, not_found_404

app = dash.Dash(__name__, use_pages=True, pages_folder="", external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page("bar_charts", layout=bar_charts.layout)
dash.register_page("heatmaps", "/", layout=heatmaps.layout)
dash.register_page("histograms", layout=histograms.layout)
dash.register_page("not_found_404", layout=not_found_404.layout)

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
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
