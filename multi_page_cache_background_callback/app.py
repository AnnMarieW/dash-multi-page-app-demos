import os
from uuid import uuid4

import dash
from dash import DiskcacheManager, CeleryManager, html, dcc
import dash_bootstrap_components as dbc

launch_uid = uuid4()

if "REDIS_URL" in os.environ:
    # Use Redis & Celery if REDIS_URL set as an env variable
    from celery import Celery

    celery_app = Celery(
        __name__, broker=os.environ["REDIS_URL"], backend=os.environ["REDIS_URL"]
    )
    background_callback_manager = CeleryManager(
        celery_app, cache_by=[lambda: launch_uid], expire=60
    )

else:
    # Diskcache for non-production apps when developing locally
    import diskcache

    cache = diskcache.Cache("./cache")
    background_callback_manager = DiskcacheManager(
        cache, cache_by=[lambda: launch_uid], expire=60
    )

app = dash.Dash(
    __name__,
    background_callback_manager=background_callback_manager,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

app.layout = dbc.Container(
    [
        dcc.Markdown(
            """
            # Background Callback with Caching Examples
            These examples are from the [Background Callback Caching](https://dash.plotly.com/background-callback-caching) section of the dash docs.  
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
        dcc.Store(id="example1_running"),
        dcc.Store(id="example3_running"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
