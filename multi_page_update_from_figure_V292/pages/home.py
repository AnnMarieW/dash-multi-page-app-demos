import dash
from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import pandas as pd

register_page(__name__, path="/")

df_airports = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv"
)
fig = px.scatter_mapbox(
    df_airports,
    lat="lat",
    lon="long",
    hover_data=["iata", "airport", "city", "state", "cnt"],
    size="cnt",
    color="cnt",
    zoom=3,
    title="Airport Traffic Data"
)
fig.update_layout(mapbox_style="open-street-map")

layout = html.Div(dcc.Graph(id="graph", figure=fig))


@callback(
    Output("url", "href"),
    Input("graph", "clickData"),
    prevent_initial_callback=True
)
def generate_chart(clickdata):
    if not clickdata:
        return dash.no_update
    airport_code = clickdata["points"][0]["customdata"][0]
    return f"/flight-status/{airport_code}"
