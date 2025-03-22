from dash import dcc, html, Output, Input,  callback, register_page

register_page(__name__, path="/")

layout = html.Div(
    [
        html.Label("Page 1 Select Year"),
        dcc.Dropdown(
            options=tuple(range(2010, 2023)),
            id="all-pages-year",
            persistence=True,
        ),
        html.Div(id="page1-out"),
    ]
)

@callback(
    Output("page1-out", "children"),
    Input("all-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"