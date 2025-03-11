import dash
from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify


app = dash.Dash(__name__, use_pages=True)


def create_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    variant="light",
                ),
                dmc.Text(label, size="sm", color="gray"),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )


sidebar = dmc.Navbar(
    fixed=True,
    width={"base": 300},
    position={"top": 80},
    height=300,
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type="scroll",
            children=[
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon="radix-icons:rocket",
                            label="Home",
                            href="/",
                        ),
                    ],
                ),
                dmc.Divider(
                    label="Chapter 1", style={"marginBottom": 20, "marginTop": 20}
                ),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter1")
                    ],
                ),
                dmc.Divider(
                    label="Chapter 2", style={"marginBottom": 20, "marginTop": 20}
                ),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter2")
                    ],
                ),
            ],
        )
    ],
)

app.layout = dmc.Container(
    [
        dmc.Header(
            height=70,
            children=[dmc.Text("Company Logo")],
            style={"backgroundColor": "#228be6"},
        ),
        sidebar,
        dmc.Container(
            dash.page_container,
            size="lg",
            pt=20,
            style={"marginLeft": 300},
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)
