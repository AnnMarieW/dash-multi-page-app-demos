from dash import  html, dcc, Output, Input,  callback, register_page

register_page(__name__, path="/page2")

layout = html.Div(
    [
        html.Label("Page 2 Select Year"),
        dcc.Dropdown(
            options=tuple(range(2010, 2023)),
            id="all-pages-year",
            persistence=True,
        ),
        html.Div(id="page2-out"),
    ]
)

@callback(
    Output("page2-out", "children"),
    Input("all-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"