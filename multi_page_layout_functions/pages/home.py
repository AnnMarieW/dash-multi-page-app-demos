from dash import html
import dash

dash.register_page(__name__, path="/", top_nav=True)


layout = html.Div("Home page content")
