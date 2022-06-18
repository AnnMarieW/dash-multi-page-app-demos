"""
Use this default figure in the layout.  It has a transparent background and no axis, which
reduces the flash when navigating to a different  pages or switching themes
e.g.
layout = html.Div(
    [
        dcc.Graph(id="heatmaps-graph", figure=default_fig)
    ]

)
"""

import plotly.express as px

default_fig = px.scatter()
default_fig.update_layout(
    paper_bgcolor="rgba(0, 0, 0, 0)",
    plot_bgcolor="rgba(0, 0, 0, 0)",
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
)
