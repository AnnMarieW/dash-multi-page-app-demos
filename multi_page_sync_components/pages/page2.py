from dash import dcc, html, register_page, ctx, no_update
from dash_extensions.enrich import Output, Input, State, callback

register_page(__name__)

years = [year for year in (range(2010, 2023))]

layout = html.Div(
    [
        html.Label("Page 2 Select Year"),
        dcc.Dropdown(years, id="page2-year"),
    ]
)


@callback(
    Output("page2-year", "value"),
    Output("store", "data"),
    Input("page2-year", "value"),
    State("store", "data"),
)
def sync_dropdowns(dd_year, store_year):
    if dd_year is None:
        return store_year, no_update
    return dd_year, dd_year
