from dash import html
import dash_bootstrap_components as dbc

path_pagename_map = {
    "/about/topic-1": "Topic 1",
    "/about/topic-2": "Topic 2",
    "/about/topic-3": "Topic 3"
}

def sidebar():
    return html.Div(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(name, className="ms-2"),
                    ],
                    href=href,
                    active="exact",
                )
                for href, name in path_pagename_map.items()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
        )
    )
