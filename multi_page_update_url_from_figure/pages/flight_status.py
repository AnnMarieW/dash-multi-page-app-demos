"""
Example of:
  -  title and description updated dynamically with a function
  - passing variables in the url pathname to the layout function.
    Using the path_template parameter in dash.register_page, you can define which segments of the path
    are variables by marking them like this: <variable_name>. The layout function then receives
    the <variable_name> as a keyword argument.
"""


from dash import html, register_page


def title(airport=None, type=None):
    return f"Flight Status for {airport}"


def description(airport=None, type=None):
    return f"Arrival and Departure status for  {airport}"


register_page(
    __name__,
    path_template="/flight-status/<airport>/<type>",
    title=title,
    description=description,
    path="/flight-status/ord/arrivals",
)


def layout(airport=None, type=None, **other_unknown_query_strings):
    return html.H3(f"Flight {type} data for: {airport}")
