from dash import Dash, html, dcc
import dash


app = Dash(__name__, use_pages=True)

# Example of creating a page without using a pages folder
dash.register_page("another_home", layout=html.Div("We're home!"), path="/")

# Example of setting an order.  The page registry is sorted by the `order` parameter, then by module name
dash.register_page(
    "very_important", layout=html.Div("Don't miss it!"), path="/important", order=0
)


app.layout = html.Div(
    [
        html.H1("App Frame"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']} - {page['path']}", href=page["path"])
                )
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ]
        ),
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
