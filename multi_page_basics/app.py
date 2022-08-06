import pandas as pd
from dash_extensions.enrich import DashProxy, dcc, html, Input, OperatorOutput, Operator, OperatorTransform
import plotly.express as px
import numpy as np
from dash.exceptions import PreventUpdate

colors = ["red", "green", "blue"]
default_color = colors[0]
data = np.random.random((5000, 2))
df = pd.DataFrame(columns=["x", "y"], data=data)

app = DashProxy(transforms=[OperatorTransform()])
app.layout = html.Div([
    dcc.Graph(id="graph", figure=px.scatter(data_frame=df, x='x', y='y', color_discrete_sequence=[default_color])),
    dcc.Dropdown(id="dd", options=colors, value=default_color)
])

@app.callback(OperatorOutput("graph", "figure"), Input("dd", "value"))
def change_color(color):
    if color is None:
        raise PreventUpdate
    return Operator()['data'][0]['marker']['color'].assign(color)

if __name__ == '__main__':
    app.run_server()