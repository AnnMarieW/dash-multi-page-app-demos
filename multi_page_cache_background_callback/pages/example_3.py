"""
can't change pages while job is running
"""


import time

import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import plotly.graph_objects as go

title = "Caching with background callback with progess bar"
dash.register_page(__name__, title=title)

df = px.data.tips()


def make_progress_graph(progress, total):
    progress_graph = (
        go.Figure(data=[go.Bar(x=[progress])])
        .update_xaxes(range=[0, total])
        .update_yaxes(
            showticklabels=False,
        )
        .update_layout(height=100, margin=dict(t=20, b=40))
    )
    return progress_graph


layout = html.Div(
    [
        html.H4(title),
        dcc.Dropdown(
            ["total_bill", "tip", "size"], "total_bill", clearable=False, id="dropdown3"
        ),
        html.Button("Cancel Running Job!", id="cancel3"),
        dcc.Graph(figure=make_progress_graph(0, 5), id="progress_bar_graph3"),
        dcc.Graph(id="graph3"),
    ]
)


@dash.callback(
    Output("graph3", "figure"),
    Output("dropdown3", "value"),
    Input("dropdown3", "value"),
    background=True,
    running=[
        (Output("dropdown3", "disabled"), True, False),
        (Output("cancel3", "disabled"), False, True),
        (
            Output("graph3", "style"),
            {"visibility": "hidden"},
            {"visibility": "visible"},
        ),
        (
            Output("progress_bar_graph3", "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
    ],
    cancel=[Input("cancel3", "n_clicks")],
    progress=Output("progress_bar_graph3", "figure"),
    progress_default=make_progress_graph(0, 5),
    interval=1000,
    # config_prevent_initial_callbacks=True,
)
def update_progress(set_progress, value):
    total = 10
    for i in range(total + 1):
        set_progress(make_progress_graph(i, 10))
        time.sleep(1)
    fig = px.pie(df, values=value, names="day", hole=0.3)
    return fig, value
