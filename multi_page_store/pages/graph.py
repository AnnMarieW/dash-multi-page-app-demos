from dash import dcc, html, Input, Output, callback, register_page
import plotly.express as px
import pandas as pd

register_page(__name__, path="/")

df = px.data.gapminder()
years = df.year.unique()

layout = html.Div(
    [
        html.Label("Select Year"),
        dcc.Dropdown(years, years[-1], id="year", clearable=False, persistence="session"),
        dcc.Graph(id="graph"),
    ]
)


@callback(
    Output("store", "data"),
    Input("year", "value"),
)
def get_data(year):
    # simulate some expensive data processing step
    # store results in a dcc.Store in app.py
    dff = df.query(f"year=={year}")
    store = {
        "data": dff.to_dict("records"),
        "columns": [{"name": i, "id": i} for i in dff.columns],
    }
    return store


@callback(
    Output("graph", "figure"),
    Input("store", "data"),
)
def update(store):
    dff = pd.DataFrame(store["data"])
    return px.scatter(
        dff,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
    )
