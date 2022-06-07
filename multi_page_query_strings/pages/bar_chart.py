import dash

dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.tips()
days = df.day.unique()


def layout(day=days[0], **other_unknown_query_strings):
    return html.Div(
        [
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": x, "value": x} for x in days],
                value=day,
                clearable=False,
            ),
            dcc.Graph(id="bar-chart"),
        ]
    )


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig
