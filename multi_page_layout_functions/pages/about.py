from dash import html
import dash

dash.register_page(__name__, top_nav=True)


layout = html.Div("About page content")
