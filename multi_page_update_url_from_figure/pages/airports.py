from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

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
)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

layout = html.Div(
    [html.H4("Airports"), dcc.Graph(id="graph", figure=fig), html.Div(id="link")]
)


@callback(
    Output("link", "children"),
    Input("graph", "clickData"),
)
def generate_chart(clickdata):
    if not clickdata:
        return ""
    airport_code = clickdata["points"][0]["customdata"][0]
    airport_name = clickdata["points"][0]["customdata"][1]

    return dbc.Card(
        dbc.CardBody(
            [
                html.H4("Flight Status", className="card-title"),
                html.H6(f"For {airport_name}", className="card-subtitle"),
                # Note: dbc.Cardlink works like a dcc.Link -- navigation without refreshing the page.
                dbc.CardLink(
                    "Arrivals", href=f"/flight-status/{airport_code}/arrivals"
                ),
                dbc.CardLink(
                    "Departures", href=f"/flight-status/{airport_code}/departures"
                ),
            ]
        ),
        style={"width": "18rem"},
    )
