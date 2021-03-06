import dash
from dash import html, callback, Input, Output
from make_cache import get_dataframe

dash.register_page(__name__)


def layout():
    return html.Div(
        [
            html.Button("Get data", id="get-data-button"),
            html.Div(id="output-1"),
            html.Div(id="output-2"),
        ]
    )


@callback(
    Output("output-1", "children"),
    Input("get-data-button", "n_clicks"),
    Input("session-id", "data"),
    prevent_initial_call=True,
)
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div(
        [
            "Output 1 - Button has been clicked {} times".format(value),
            html.Pre(df.to_csv()),
        ]
    )


@callback(
    Output("output-2", "children"),
    Input("get-data-button", "n_clicks"),
    Input("session-id", "data"),
    prevent_initial_call=True,
)
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div(
        [
            "Output 2 - Button has been clicked {} times".format(value),
            html.Pre(df.to_csv()),
        ]
    )
