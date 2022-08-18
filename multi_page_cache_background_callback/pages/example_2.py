import time
import dash
from dash import  dcc, html, Input, Output, callback
import plotly.express as px

title = "Enable caching - with dropdown and figure"
dash.register_page(__name__, title=title)

df = px.data.tips()

dropdown = dcc.Dropdown(
    ["Fri", "Sat", "Sun"],
    "Fri",
    clearable=False,
    persistence=True,
    id="dropdown2",
)
graph = dcc.Graph()

layout = html.Div([html.H4(title), dropdown, dcc.Loading(graph)])


@callback(
    Output(graph, "figure"),
    Output("dropdown2", "value"),
    Input("dropdown2", "value"),
    background=True,
)
def update_bar_chart(day):
    # simulate long calculation
    time.sleep(5)
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig, day
