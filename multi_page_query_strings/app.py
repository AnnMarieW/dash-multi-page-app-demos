import dash
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


navbar = dbc.NavbarSimple(
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
    ),
    brand="Multi Page App Demo: Query Strings",
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
