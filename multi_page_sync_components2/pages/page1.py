from dash import dcc, html, register_page, no_update
from dash_extensions.enrich import Output, Input, State, callback

register_page(__name__, path="/")

years = [year for year in (range(2010, 2023))]

layout = html.Div(
    [
        html.Label("Page 1 Select Year"),
        dcc.Dropdown(years, id="page1-year"),
        html.Div(id="page1-out"),
    ]
)


@callback(
    Output("page1-year", "value"),
    Output("store", "data"),
    Input("page1-year", "value"),
    State("store", "data"),
)
def sync_dropdowns(dd_year, store_year):
    if dd_year is None:
        return store_year, no_update
    return dd_year, dd_year


@callback(Output("page1-out", "children"), Input("page1-year", "value"))
def update(year):
    return f"The dropdown is {year}"
