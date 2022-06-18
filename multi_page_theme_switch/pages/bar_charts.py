import dash
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
from dash_bootstrap_templates import ThemeSwitchAIO
from pages.default_fig import default_fig

template_theme2 = "flatly"
template_theme1 = "darkly"


dash.register_page(__name__)

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
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_bar_chart(day, toggle):
    template = template_theme1 if toggle else template_theme2
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
