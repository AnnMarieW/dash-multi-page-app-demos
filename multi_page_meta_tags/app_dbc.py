import dash
from dash import html
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


pages_dropdown = dbc.DropdownMenu(
    [
        dbc.DropdownMenuItem(
            children=html.Div(
                [
                    html.Img(
                        src=app.get_asset_url(page["image"]),
                        height="60px",
                        width="80px",
                    ),
                    page["name"],
                ]
            ),
            href=page["path"],
        )
        for page in dash.page_registry.values()
    ],
    nav=True,
    label="More Pages",
    toggle_class_name="text-white",
)
#
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(
                            html.Img(src=app.get_asset_url("logo.jpeg"), height="50px")
                        ),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
            ),
            pages_dropdown,
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
)
#

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container,
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
