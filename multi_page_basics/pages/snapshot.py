# example of matching a path that starts with "shapshot-"

import dash

dash.register_page(
    __name__,
    path_template="/snapshot-<snapshot_id>",
)


def layout(snapshot_id=None, **other_unknown_query_strings):
    return dash.html.Div(f"snapshot page:  snapshot-{snapshot_id}")
