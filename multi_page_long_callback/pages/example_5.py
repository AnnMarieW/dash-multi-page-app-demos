import time
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

import ids

title = "Example 5: Progress Bar Chart Graph"
dash.register_page(__name__, title=title)


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
        html.P(id=ids.EXAMPLE_5_P, children=["Button not clicked"]),
        dcc.Graph(
            id=ids.EXAMPLE_5_PROGRESS_BAR_GRAPH, figure=make_progress_graph(0, 10)
        ),
        html.Button(id=ids.EXAMPLE_5_BUTTON, children="Run Job!"),
        html.Button(id=ids.EXAMPLE_5_CANCEL, children="Cancel Running Job!"),
    ]
)


@dash.callback(
    output=Output(ids.EXAMPLE_5_P, "children"),
    inputs=Input(ids.EXAMPLE_5_BUTTON, "n_clicks"),
    background=True,
    running=[
        (Output(ids.EXAMPLE_5_BUTTON, "disabled"), True, False),
        (Output(ids.EXAMPLE_5_CANCEL, "disabled"), False, True),
        (
            Output(ids.EXAMPLE_5_P, "style"),
            {"visibility": "hidden"},
            {"visibility": "visible"},
        ),
        (
            Output(ids.EXAMPLE_5_PROGRESS_BAR_GRAPH, "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
    ],
    cancel=[Input(ids.EXAMPLE_5_CANCEL, "n_clicks")],
    progress=Output(ids.EXAMPLE_5_PROGRESS_BAR_GRAPH, "figure"),
    progress_default=make_progress_graph(0, 10),
    interval=1000,
    config_prevent_initial_callbacks=True,
)
def update_progress(set_progress, n_clicks):
    total = 10
    for i in range(total+1):
        set_progress(make_progress_graph(i, 10))
        time.sleep(1)
    return [f"Clicked {n_clicks} times"]
