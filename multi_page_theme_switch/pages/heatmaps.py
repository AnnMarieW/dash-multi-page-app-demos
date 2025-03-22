
import dash_bootstrap_components as dbc
from .default_fig import default_fig
from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px


register_page(__name__, path="/")
df = px.data.medals_wide(indexed=True)


layout = html.Div(
    [
        html.P("Medals included:"),
        dbc.Checklist(
            id="heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.tolist(),
        ),
        dcc.Graph(id="heatmaps-graph", figure=default_fig),
    ]
)


@callback(
    Output("heatmaps-graph", "figure"),
    Input("heatmaps-medals", "value"),
    Input("switch", "value"),
)
def filter_heatmap(cols, toggle):
    fig = px.imshow(df[cols], template="flatly" if toggle else "flatly_dark")
    return fig
