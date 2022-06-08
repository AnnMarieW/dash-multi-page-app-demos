import dash
from dash import  html, callback, Input, Output

from make_cache import get_dataframe

dash.register_page(__name__)


def layout():
    return html.Div(
        [
            html.Button("Get data", id="get-data-button2"),
            html.Div(id="output-3"),
            html.Div(id="output-4"),
        ]
    )


@callback(
    Output("output-3", "children"),
    Input("get-data-button2", "n_clicks"),
    Input("session-id", "data"),
    prevent_initial_call=True,
)
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div(
        [
            "Output 3 - Button has been clicked {} times".format(value),
            html.Pre(df.to_csv()),
        ]
    )


@callback(
    Output("output-4", "children"),
    Input("get-data-button2", "n_clicks"),
    Input("session-id", "data"),
    prevent_initial_call=True,
)
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div(
        [
            "Output 4 - Button has been clicked {} times".format(value),
            html.Pre(df.to_csv()),
        ]
    )
