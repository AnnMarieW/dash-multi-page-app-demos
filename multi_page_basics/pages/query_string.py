"""
Example of passing query strings from the url to a layout function
"""


import dash

dash.register_page(__name__, path="/dashboard")


def layout(velocity=None, **other_unknown_query_strings):
    return dash.html.Div(id="velocity", children=f"velocity={velocity}")
