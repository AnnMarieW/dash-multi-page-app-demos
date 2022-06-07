import dash
from dash import html, get_asset_url


dash.register_page(
    __name__,
    description="Welcome to my app",
    redirect_from=["/old-home-page", "/v2"],
    extra_template_stuff="yup",
)

layout = html.Div(
    ["Home Page", html.Img(src=get_asset_url("birds.jpeg"), height="50px")]
)
