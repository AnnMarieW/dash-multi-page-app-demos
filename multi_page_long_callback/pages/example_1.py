import time
import dash
from dash import html, Output, Input
import ids

title = "Example 1 - Simple Example"
dash.register_page(__name__, path="/", title=title)

layout = html.Div(
    [
        html.H4(title),
        html.P(id=ids.EXAMPLE_1_P, children=["Button not clicked"]),
        html.Button(id=ids.EXAMPLE_1_BUTTON, children="Run Job!"),
    ]
)


@dash.callback(
    output=Output(ids.EXAMPLE_1_P, "children"),
    inputs=Input(ids.EXAMPLE_1_BUTTON, "n_clicks"),
    background=True,
    config_prevent_initial_callbacks=True,
)
def update_clicks(n_clicks):
    time.sleep(2.0)
    return [f"Clicked {n_clicks} times"]
