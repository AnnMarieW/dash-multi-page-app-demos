import time
import dash
from dash import html, Input, Output
import ids

title = "Example 4: Progress Bar"
dash.register_page(__name__, title=title)


layout = html.Div(
    [
        html.H4(title),
        html.P(id=ids.EXAMPLE_4_P, children=["Button not clicked"]),
        html.Div(
            html.Progress(id=ids.EXAMPLE_4_PROGRESS_BAR, style={"visibility": "hidden"})
        ),
        html.Button(id=ids.EXAMPLE_4_BUTTON, children="Run Job!"),
        html.Button(id=ids.EXAMPLE_4_CANCEL, children="Cancel Running Job!"),
    ]
)


@dash.callback(
    output=Output(ids.EXAMPLE_4_P, "children"),
    inputs=Input(ids.EXAMPLE_4_BUTTON, "n_clicks"),
    background=True,
    running=[
        (Output(ids.EXAMPLE_4_BUTTON, "disabled"), True, False),
        (Output(ids.EXAMPLE_4_CANCEL, "disabled"), False, True),
        (
            Output(ids.EXAMPLE_4_P, "style"),
            {"display": "hidden"},
            {"visibility": "visible"},
        ),
        (
            Output(ids.EXAMPLE_4_PROGRESS_BAR, "style"),
            {"visibility": "visible"},
            {"visibility": "hidden"},
        ),
    ],
    cancel=[Input(ids.EXAMPLE_4_CANCEL, "n_clicks")],
    progress=[
        Output(ids.EXAMPLE_4_PROGRESS_BAR, "value"),
        Output(ids.EXAMPLE_4_PROGRESS_BAR, "max"),
    ],
    config_prevent_initial_callbacks=True,
)
def update_progress(set_progress, n_clicks):
    total = 10
    for i in range(total):
        time.sleep(0.5)
        set_progress((str(i + 1), str(total)))
    return [f"Clicked {n_clicks} times"]
