from dash import Dash, html, dcc
import dash


app = Dash(__name__, use_pages=True)


app.layout = html.Div(
    [
        html.H1("App Frame"),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src=app.get_asset_url(page["image"]),
                            height="40px",
                            width="60px",
                        ),
                        dcc.Link(f"{page['name']} - {page['path']}", href=page["path"]),
                    ],
                    style={"margin": 20},
                )
                for page in dash.page_registry.values()
            ]
        ),
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run(debug=True)
