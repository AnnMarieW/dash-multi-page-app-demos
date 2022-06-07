from dash import dcc, html
import dash

dash.register_page(__name__, path="/")


layout = html.Div(
    [
        html.Div(
            "This is a demo of how to use query strings to pass variables to other pages of a multi-page app: "
        ),
        html.Span(
            [
                "See the bar chart page with tips data for ",
                dcc.Link("Saturday ", href="/bar-chart?day=Sat"),
                "or for ",
                dcc.Link("Sunday ", href="/bar-chart?day=Sun"),
            ]
        ),
    ]
)
