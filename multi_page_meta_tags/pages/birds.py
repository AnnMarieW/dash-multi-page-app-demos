import dash

dash.register_page(
    __name__,
    title="(birds) The title, headline or name of the page",
    description="(birds) A short description or summary 2-3 sentences",
)


def layout():
    return """
    No image is specified but it's inferred from the module name.
    The module name is`birds.py` so it uses the `birds.jpeg` file in the assets folder.
    """
