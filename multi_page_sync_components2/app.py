"""
 This example demonstrates syncing components between pages of a multi-page app.

 For syncing component, please start with simpler version:  multi_page_sync_components.
 If that doesn't work (such as when the component is updated in the callback or the
 persistence prop cannot be set), then try this version.  (v2)

 Note that dcc.Store is in the app.py file so that it's accessible in all pages.

 required dash>=2.9.2 to allow duplicate callback outputs

"""


from dash import Dash, html, dcc, page_registry, page_container


years = [str(year) for year in (range(2020, 2023))]

app = Dash(
    __name__,
    use_pages=True,
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
    app.run_server(debug=True)
