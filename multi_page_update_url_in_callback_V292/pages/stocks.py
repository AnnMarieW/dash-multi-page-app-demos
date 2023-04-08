"""
Example of:
  -  title and description updated dynamically with a function
  - passing variables in the url pathname to the layout function.
    Using the path_template parameter in dash.register_page, you can define which segments of the path
    are variables by marking them like this: <variable_name>. The layout function then receives
    the <variable_name> as a keyword argument.
  - using urllib.parse.unquote to get decoded strings from the url
"""

from urllib.parse import unquote
from dash import html, register_page


def title(ticker=None):
    return f"{unquote(ticker)} Analysis"


def description(ticker=None):
    return f"News, financials and technical analysis for {unquote(ticker)}"


register_page(
    __name__,
    path_template="/stocks/<ticker>",
    title=title,
    description=description,
    path="/stocks/aapl",
)


def layout(ticker=None, **other_unknown_query_strings):
    if ticker:
        ticker = unquote(ticker)
    return html.H3(f"Financial and Technical Analysis for: {ticker}")
