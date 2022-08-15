import os

import dash
from dash import DiskcacheManager, CeleryManager, dcc, html

if "REDIS_URL" in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery

    celery_app = Celery(
        __name__, broker=os.environ["REDIS_URL"], backend=os.environ["REDIS_URL"]
    )
    background_callback_manager = CeleryManager(celery_app)

else:
    # Diskcache for non-production apps when developing locally
    import diskcache

    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(cache)

app = dash.Dash(
    __name__, use_pages=True, background_callback_manager=background_callback_manager,
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            # Background Callbacks (long callbacks) Examples
            These examples are from the [Background Callbacks](https://dash.plotly.com/background-callbacks) section of the dash docs.  
            Each example is a page of a multi-page app. Requires dash>=2.6.1
             
             
            """
        ),
        html.Div(
            [
                html.Div(dcc.Link(f"{page['title']}", href=page["path"]))
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ]
        ),
        html.Hr(),
        dash.page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
