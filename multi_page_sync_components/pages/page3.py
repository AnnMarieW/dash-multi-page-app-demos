from dash import dcc, html, Output, Input, callback, register_page

register_page(__name__, path="/page3")

layout = html.Div(
    [
        html.Label("Page 3 Select Year"),
        dcc.Dropdown(
            options=tuple(range(2010, 2023)),
            id="all-pages-year",
            persistence=True,
        ),
        html.Div(id="page3-out"),
    ]
)

@callback(
    Output("page3-out", "children"),
    Input("all-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"