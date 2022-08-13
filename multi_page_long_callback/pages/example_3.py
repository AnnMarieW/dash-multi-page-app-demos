import time
import dash
from dash import html, Input, Output
import ids

title = "Example 3: Cancelable Callback"
dash.register_page(__name__, title=title)


layout = html.Div(
    [
        html.H4(title),
        html.P(id=ids.EXAMPLE_3_P, children=["Button not clicked"]),
        html.Button(id=ids.EXAMPLE_3_BUTTON, children="Run Job!"),
        html.Button(id=ids.EXAMPLE_3_CANCEL, children="Cancel Running Job!"),
    ]
)


@dash.callback(
    output=Output(ids.EXAMPLE_3_P, "children"),
    inputs=Input(ids.EXAMPLE_3_BUTTON, "n_clicks"),
    background=True,
    running=[
        (Output(ids.EXAMPLE_3_BUTTON, "disabled"), True, False),
        (Output(ids.EXAMPLE_3_CANCEL, "disabled"), False, True),
    ],
    cancel=[Input(ids.EXAMPLE_3_CANCEL, "n_clicks")],
    config_prevent_initial_callbacks=True,
)
def update_clicks(n_clicks):
    time.sleep(3.0)
    return [f"Clicked {n_clicks} times"]
