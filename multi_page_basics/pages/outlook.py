"""
Example of
  - adding a custom title, description, and image which will be used to create the meta-tags.
  - setting a pathname for the page.
"""

import dash
from dash import html

dash.register_page(
    __name__,
    title="Forward Outlook",
    description="This is the forward outlook",
    image="birds.jpeg",
    path="/forward-outlook",
)


layout = html.Div("Forward outlook")
