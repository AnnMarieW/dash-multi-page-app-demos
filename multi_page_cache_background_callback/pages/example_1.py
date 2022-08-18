import time
import dash
from dash import Input, Output, html
import dash_bootstrap_components as dbc

title = "Enabling Caching - example from the dash docs"
dash.register_page(__name__, path="/", title=title)

layout = html.Div(
    [
        html.H4(title),
        html.P(
            "The first 4 times the button is clicked, it's slow. After that, cached values are used"
        ),
        html.Div([html.P(id="paragraph1_id", children=["Button not clicked"])]),
        dbc.Button(id="button1_id", children="Run Job!"),
        dbc.Button(id="cancel_button1_id", children="Cancel Running Job!"),
    ]
)


@dash.callback(
    output=(Output("paragraph1_id", "children"), Output("button1_id", "n_clicks")),
    inputs=Input("button1_id", "n_clicks"),
    background=True,
    running=[(Output("example1_running", "data"), True, False)],
    cancel=Input("cancel_button1_id", "n_clicks"),
    config_prevent_initial_callbacks=True,
)
def update_clicks(n_clicks):
    time.sleep(10.0)
    return [f"Clicked {n_clicks} times"], (n_clicks or 0) % 4


@dash.callback(
    Output("button1_id", "disabled"),
    Output("cancel_button1_id", "disabled"),
    Input("example1_running", "data"),
)
def disable(running):
    # disable the run and cancel button based on whether the callback is running
    return running, not running
