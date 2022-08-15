import time
import dash
from dash import html, Input, Output
import ids

title = "Example 2: Disable Button While Callback Is Running"
dash.register_page(__name__, title=title)


layout = html.Div(
    [
        html.H4(title),
        html.P(id=ids.EXAMPLE_2_P, children=["Button not clicked"]),
        html.Button(id=ids.EXAMPLE_2_BUTTON, children="Run Job!"),
    ]
)


@dash.callback(
    output=Output(ids.EXAMPLE_2_P, "children"),
    inputs=Input(ids.EXAMPLE_2_BUTTON, "n_clicks"),
    background=True,
    running=[
        (Output(ids.EXAMPLE_2_BUTTON, "disabled"), True, False),
    ],
    config_prevent_initial_callbacks=True,
)
def update_clicks(n_clicks):
    print("in E2 callback")
    time.sleep(4.0)
    return [f"Clicked {n_clicks} times"]
