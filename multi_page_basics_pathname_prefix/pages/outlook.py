import dash

dash.register_page(
    __name__,
    title="Forward Outlook",
    description="This is the forward outlook",  # should accept callable too
    path="/forward-outlook",
    image="birds.jpeg",
)


def layout():
    return "Forward outlook"
