import dash
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc


app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],
)


navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if not page["path"].startswith("/chapter")
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo",
    color="primary",
    dark=True,
    className="mb-2",
)

sidebar_button = dbc.Button(html.I(className="fa fa-bars"), id="sidebar-btn")
sidebar = dbc.Offcanvas(
    dbc.Nav(
        [html.H3("Chapters")]
        + [
            dbc.NavLink(
                [
                    html.I(className=page["icon"]),
                    html.Span(page["name"], className="ms-2"),
                ],
                href=page["path"],
                active="exact",
            )
            for page in dash.page_registry.values()
            if page["path"].startswith("/chapter")
        ],
        vertical=True,
        pills=True,
    ),
    id="offcanvas",
)

app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dbc.Col([sidebar_button], width=1),
                dbc.Col([sidebar, dash.page_container]),
            ]
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("offcanvas", "is_open"),
    Input("sidebar-btn", "n_clicks"),
    State("offcanvas", "is_open"),
)
def toggle_theme_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)
