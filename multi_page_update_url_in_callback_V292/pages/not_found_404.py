"""
Example of creating a custom 404 page to display when the URL isn't found
"""


from dash import html, register_page
import dash

register_page(__name__, path="/404")


layout = html.H1("Custom 404")
