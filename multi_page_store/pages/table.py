from dash import html, dash_table, Input, Output, callback, register_page

register_page(__name__)

layout = html.Div(id="table-output")


@callback(
    Output("table-output", "children"),
    Input("store", "data"),
)
def update(store):
    if store == {}:
        return "Select year on the graph page"
    return dash_table.DataTable(
        page_size=10,
        data=store.get("data"),
        columns=store.get("columns"),
        filter_action="native",
        sort_action="native",
        style_table={"overflowX": "auto"},
    )
