from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px

register_page(__name__, icon="fa:pie-chart")

# This dataframe has 244 lines, but 4 distinct values for `day`
df = px.data.tips()


layout = html.Div(
    [
        dmc.Text("Names:"),
        dmc.Select(
            id="names",
            value="day",
            data=[{"value": x, "label": x} for x in ["smoker", "day", "time", "sex"]],
            clearable=False,
        ),
        dmc.Space(h=20),
        dmc.Text("Values:"),
        dmc.Select(
            id="values",
            value="total_bill",
            data=[{"value": x, "label": x} for x in ["total_bill", "tip", "size"]],
            clearable=False,
        ),
        dcc.Graph(id="pie-chart"),
    ]
)


@callback(
    Output("pie-chart", "figure"), [Input("names", "value"), Input("values", "value")]
)
def generate_chart(names, values):
    fig = px.pie(df, values=values, names=names)
    return fig
