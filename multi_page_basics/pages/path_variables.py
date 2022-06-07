"""
Example of:
  -  title and description updated dynamically with a function
  - passing variables in the url pathname to the layout function.
    Using the path_template parameter in dash.register_page, you can define which segments of the path
    are variables by marking them like this: <variable_name>. The layout function then receives
    the <variable_name> as a keyword argument.
"""

import dash


def title(asset_id=None, dept_id=None):
    return f"Asset Analysis: {asset_id} {dept_id}"


def description(asset_id=None, dept_id=None):
    return f"This is the AVN Industries Asset Analysis: {asset_id} in {dept_id}"


dash.register_page(
    __name__,
    path_template="/asset/<asset_id>/department/<dept_id>",
    title=title,
    description=description,
    path="/asset/inventory/department/branch-1001",
)


def layout(asset_id=None, dept_id=None, **other_unknown_query_strings):
    return dash.html.Div(
        f"variables from pathname:  asset_id: {asset_id} dept_id: {dept_id}"
    )
