"""
 This example demonstrates an easy way of syncing components between pages of a multi-page app.
 It uses the same dropdown component on each page and sets `persistence=True`

 If persistence doesn't work (such as when you update the component in a callback),
 try using muti_page_sync_components2 which uses a dcc.Store to track the values
"""


from dash import Dash, html, dcc, page_registry, page_container


app = Dash(use_pages=True)

app.layout = html.Div(
    [
        html.H1("Multi Page App Demo: Sync components between pages"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']}", href=page["path"]),
                )
                for page in page_registry.values()
            ]
        ),
        html.Hr(),
        page_container,
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
