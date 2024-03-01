from dash import html
import dash_bootstrap_components as dbc
import dash

from .side_bar import sidebar
from .topic_1 import layout_1
from .topic_2 import layout_2
from .topic_3 import layout_3

def title(topic=None):
    # This will show in browser tab and the meta tags
    return f"About page: {topic}"


def description(topic=None):
    # This is the description for the meta tags.  It will show when you share a link to this page.
    if topic == "topic1":
        return "Here is more information on topic 1"
    return "Here is general info about the topics on this page"


dash.register_page(
    __name__,
    path_template="/about/<topic>",
    title=title,
    description=description,
    # sets a default for the path variable
    path="/about/topic-1",
    # prevents showing a Page Not Found if someone enters /about in the browser
    redirect_from=["/about", "/about/"],
)


def layout(topic=None, **other_unknown_query_strings):
    parent_card =  dbc.Card(" Here is the main About Page content", body=True)

    if topic == "topic-1":
        topic_card =  layout_1()
    elif topic == "topic-2":
        topic_card =  layout_2
    elif topic == "topic-3":
        topic_card =  layout_3
    else:
        topic_card= ""

    return dbc.Row(
        [dbc.Col(sidebar(), width=2), dbc.Col([parent_card, topic_card], width=10)]
    )


