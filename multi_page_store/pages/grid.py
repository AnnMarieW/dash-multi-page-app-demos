from dash import html,  Input, Output, callback, register_page
import dash_ag_grid as dag
import pandas as pd

register_page(__name__)

columnDefs = [
    {"field": "country"},
    {"field": "continent"},
    {"field": "year"},
    {
        "headerName": "Life Expectancy",
        "field": "lifeExp",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('.1f')(params.value)"},
    },
    {
        "headerName": "Population",
        "field": "pop",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format(',.0f')(params.value)"},
    },
    {
        "headerName": "GDP per Capita",
        "field": "gdpPercap",
        "type": "rightAligned",
        "valueFormatter": {"function": "d3.format('$,.1f')(params.value)"},
    },
]

layout = html.Div(id="grid-output")


@callback(
    Output("grid-output", "children"),
    Input("store", "data"),
)
def update(store):
    if store == {}:
        return "Select year on the graph page"
    dff = pd.DataFrame(store)

    return dag.AgGrid(
        columnDefs=columnDefs,
        rowData=dff.to_dict("records"),
        columnSize="sizeToFit",
    )