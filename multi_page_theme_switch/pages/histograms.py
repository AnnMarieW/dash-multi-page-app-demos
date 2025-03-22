from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import numpy as np

from .default_fig import default_fig

register_page(__name__)


np.random.seed(2020)

layout = html.Div(
    [
        dcc.Graph(id="histograms-graph", figure=default_fig),
        html.P("Mean:"),
        dcc.Slider(
            id="histograms-mean", min=-3, max=3, value=0, marks={-3: "-3", 3: "3"}
        ),
        html.P("Standard Deviation:"),
        dcc.Slider(id="histograms-std", min=1, max=3, value=1, marks={1: "1", 3: "3"}),
    ]
)


@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
    Input("switch", "value"),
)
def display_color(mean, std, switch_on):
    data = np.random.normal(mean, std, size=500)
    template = "flatly" if switch_on else "flatly_dark"
    fig = px.histogram(data, nbins=30, range_x=[-10, 10], template=template)
    return fig
