"""
 This example demonstrates syncing components between pages of a multi-page app.
 Note that dcc.Store is in the app.py file so that it's accessible in all pages.
 Uses MultiplexerTransform from dash-extensions to handle multiple callbacks updating the same output.
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
    app.run_server(debug=True)
