import dash
from dash import html


dash.register_page(
    __name__,
    path="/",
    image="birdhouse.jpeg",
    title="(home) The title, headline or name of the page",
    description="(home) A short description or summary 2-3 sentences",
)


layout = html.Div("The image for the home page is specified as `birdhouse.jpeg'")
