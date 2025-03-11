"""
 This example demonstrates an easy way of syncing components between pages of a multi-page app.
 It uses the same component on each page and sets `persistence=True`

 If persistence doesn't work (such as when you update the component in a callback),
 try using muti_page_sync_components2 which uses a dcc.Store to track the values and dash-extensions MultiplexerTransform
 to update the same prop from multiple callbacks.

 This example was contributed by @nopria.  See more information at https://github.com/nopria/dash-persistence-test

"""


from dash import page_registry, page_container

from dash_extensions.enrich import (
    DashProxy,
    MultiplexerTransform,
    html,
    dcc,
)

years = [str(year) for year in (range(2020, 2023))]

app = DashProxy(
    __name__,
    transforms=[MultiplexerTransform()],
    use_pages=True,
    prevent_initial_callbacks=True,
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    [
        dcc.Store(id="store", data=2022),
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
