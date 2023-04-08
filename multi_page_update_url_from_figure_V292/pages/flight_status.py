
from dash import  html, register_page

register_page( __name__, path_template="/flight-status/<airport>")

def layout(airport=None,  **other_unknown_query_strings):
    return html.H3(f"Arrivals and Departures for: {airport}")

