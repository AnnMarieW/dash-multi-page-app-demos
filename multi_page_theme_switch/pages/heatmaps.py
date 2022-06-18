import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from pages.default_fig import default_fig


template_theme2 = "flatly"
template_theme1 = "darkly"

dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.medals_wide(indexed=True)


layout = html.Div(
    [
        html.P("Medals included:"),
        dbc.Checklist(
            id="heatmaps-medals",
            options=[{"label": x, "value": x} for x in df.columns],
            value=df.columns.tolist(),
        ),
        dcc.Graph(id="heatmaps-graph", figure=default_fig),
    ]
)


@callback(
    Output("heatmaps-graph", "figure"),
    Input("heatmaps-medals", "value"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def filter_heatmap(cols, toggle):
    fig = px.imshow(df[cols], template=template_theme1 if toggle else template_theme2)
    return fig
