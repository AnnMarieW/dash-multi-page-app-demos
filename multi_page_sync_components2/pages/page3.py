from dash import dcc, html, register_page, no_update, Output, Input, State, callback


register_page(__name__)

years = [year for year in (range(2010, 2023))]

layout = html.Div(
    [
        html.Label("Page 3 Select Year"),
        dcc.Dropdown(years, id="page3-year"),
    ]
)


@callback(
    Output("page3-year", "value"),
    Output("store", "data", allow_duplicate=True),
    Input("page3-year", "value"),
    State("store", "data"),
    prevent_initial_call=True
)
def sync_dropdowns(dd_year, store_year):
    if dd_year is None:
        return store_year, no_update
    return dd_year, dd_year
