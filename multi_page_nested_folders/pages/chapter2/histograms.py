from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import numpy as np


register_page(__name__, icon="mdi:chart-histogram")

np.random.seed(2020)

layout = html.Div(
    [
        dcc.Graph(id="histograms-graph"),
        html.P("Mean:"),
        dmc.Slider(
            id="histograms-mean",
            min=-3,
            max=3,
            value=0,
            marks=[
                {"value": -3, "label": "-3"},
                {"value": 3, "label": "3"},
            ],
        ),
        html.P("Standard Deviation:"),
        dmc.Slider(
            id="histograms-std",
            min=1,
            max=3,
            value=1,
            marks=[
                {"value": 1, "label": "1"},
                {"value": 3, "label": "3"},
            ],
        ),
    ]
)


@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.histogram(data, nbins=30, range_x=[-10, 10])
    return fig
