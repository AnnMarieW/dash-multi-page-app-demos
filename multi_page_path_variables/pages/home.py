from dash import html
import dash

dash.register_page(__name__, path="/")


layout = html.Div("Home page content")
