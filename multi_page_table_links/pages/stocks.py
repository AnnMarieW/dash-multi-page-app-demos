"""
Example of:
  -  title and description updated dynamically with a function
  - passing variables in the url pathname to the layout function.
    Using the path_template parameter in dash.register_page, you can define which segments of the path
    are variables by marking them like this: <variable_name>. The layout function then receives
    the <variable_name> as a keyword argument.
"""

import dash


def title(ticker=None):
    return f"{ticker} Analysis"


def description(ticker=None):
    return f"News, financials and technical analysis for {ticker}"


dash.register_page(
    __name__,
    path_template="/stocks/<ticker>",
    title=title,
    description=description,
    path="/stocks/aapl",
)


def layout(ticker=None, **other_unknown_query_strings):
    return dash.html.Div(f"Get ticker from the pathname:  ticker: {ticker}")
