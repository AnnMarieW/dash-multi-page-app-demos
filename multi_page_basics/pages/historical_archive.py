"""
Example of the register_page defaults
"""


from dash import html

import dash

dash.register_page(__name__)


layout = html.H1("Historical Archive")
