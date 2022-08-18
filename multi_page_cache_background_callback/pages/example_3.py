import time
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import dash_bootstrap_components as dbc

title = "Caching with background callback with progress bar"
dash.register_page(__name__, title=title)

df = px.data.tips()

layout = dbc.Container(
    [
        html.H4(title),
        dcc.Dropdown(
            ["total_bill", "tip", "size"],
            "total_bill",
            clearable=False,
            id="dropdown3",
            persistence=True,
            style={"minWidth": 300},
        ),
        dbc.Button("Cancel Running Job", id="cancel3", className="m-3"),
        dbc.Progress(id="progress3", max=10),
        dcc.Graph(id="graph3"),
    ]
)


@callback(
    Output("graph3", "figure"),
    Output("dropdown3", "value"),
    Input("dropdown3", "value"),
    background=True,
    running=[(Output("example3_running", "data"), True, False)],
    cancel=[Input("cancel3", "n_clicks")],
    progress=Output("progress3", "value"),
    # config_prevent_initial_callbacks=True,
)
def update_progress(set_progress, value):
    for i in range(11):
        set_progress(i)
        time.sleep(1)
    fig = px.pie(df, values=value, names="day", hole=0.3)
    return fig, value


@callback(
    Output("dropdown3", "disabled"),
    Output("cancel3", "disabled"),
    Output("graph3", "style"),
    Output("progress3", "style"),
    Input("example3_running", "data"),
)
def disable(running):
    disable_dropdown = False
    disable_cancel = True
    display_graph = {"visibility": "visible"}
    display_progress = {"visibility": "hidden"}
    if running:
        disable_dropdown = True
        disable_cancel = False
        display_graph = {"visibility": "hidden"}
        display_progress = {"visibility": "visible"}
    return disable_dropdown, disable_cancel, display_graph, display_progress
