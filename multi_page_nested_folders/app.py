import dash
from dash import callback, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# Set "mantine_light" as the default plotly figure template
# styles Plotly figures with Mantine theme https://www.dash-mantine-components.com/components/figure-templates
dmc.add_figure_templates(default="mantine_light")

app = dash.Dash(__name__, use_pages=True, external_stylesheets=dmc.styles.ALL)


def create_nav_link(icon, label, href):
    return dmc.NavLink(
        label=label,
        href=href,
        active="exact",
        leftSection=DashIconify(icon=icon)

    )

navbar_links =dmc.Box(
    [
       create_nav_link(
                    icon="radix-icons:rocket",
                    label="Home",
                    href="/",
                ),
        dmc.Divider(
            label="Chapter 1", style={"marginBottom": 20, "marginTop": 20}
        ),
        dmc.Stack(
            [
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
            [
                create_nav_link(
                    icon=page["icon"], label=page["name"], href=page["path"]
                )
                for page in dash.page_registry.values()
                if page["path"].startswith("/chapter2")
            ],
        ),
    ],
)

layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Title("Demo App", c="blue"),
                ],
                h="100%",
                px="md",
            )
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=navbar_links,
            p="md",
        ),
        dmc.AppShellMain(dash.page_container),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 300,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)


app.layout = dmc.MantineProvider(layout)


@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


if __name__ == "__main__":
    app.run(debug=True)
