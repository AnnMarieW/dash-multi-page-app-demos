import time

import dash
from dash import Input, Output, html

title = "Enabling Caching - example from the dash docs"
dash.register_page(__name__, path="/", title=title)

layout = html.Div(
    [
        html.H4(title),
        html.P(
            "The first 4 times the button is clicked, it's slow. After that, cached values are used"
        ),
        html.Div([html.P(id="paragraph_id", children=["Button not clicked"])]),
        html.Button(id="button_id", children="Run Job!"),
        html.Button(id="cancel_button_id", children="Cancel Running Job!"),
    ]
)


@dash.callback(
    output=(Output("paragraph_id", "children"), Output("button_id", "n_clicks")),
    inputs=Input("button_id", "n_clicks"),
    background=True,
    running=[
        (Output("button_id", "disabled"), True, False),
        (Output("cancel_button_id", "disabled"), False, True),
    ],
    cancel=[Input("cancel_button_id", "n_clicks")],
    config_prevent_initial_callbacks=True,
)
def update_clicks(n_clicks):
    time.sleep(4.0)
    return [f"Clicked {n_clicks} times"], (n_clicks or 0) % 4
