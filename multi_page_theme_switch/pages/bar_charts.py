from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
from .default_fig import default_fig

register_page(__name__)

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
        ),
        dcc.Graph(id="bar-chart", figure=default_fig),
    ]
)


@callback(
    Output("bar-chart", "figure"),
    Input("dropdown", "value"),
    Input("switch", "value"),
)
def update_bar_chart(day, toggle):
    template = "flatly" if toggle else "flatly_dark"
    mask = df["day"] == day
    fig = px.bar(
        df[mask],
        x="sex",
        y="total_bill",
        color="smoker",
        barmode="group",
        template=template,
    )
    return fig
