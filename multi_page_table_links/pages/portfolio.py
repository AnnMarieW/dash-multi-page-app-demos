"""
Example of using dcc.Link in AG Grid to  navigate to another page.

"""

import dash_ag_grid as dag
from dash import  html, dcc, register_page
import pandas as pd

register_page(__name__, path="/")

data = {
    "ticker": ["AAPL", "MSFT", "AMZN", "GOOGL"],
    "company": ["Apple", "Microsoft", "Amazon", "Alphabet"],
    "shares": [75, 40, 100, 50],
}
df = pd.DataFrame(data)

columnDefs = [
    {
        "headerName": "Stock Ticker",
        "field": "ticker",
        # stockLink function is defined in the dashAgGridComponentFunctions.js in assets folder
        "cellRenderer": "StockLink",
    },
    {"field": "company"},
    {"field": "shares" },
]


grid = dag.AgGrid(
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    columnSize="sizeToFit",
)


layout = html.Div(
    [dcc.Markdown("Adding dcc.Link in cells  with cellRenderer"), grid],
    style={"margin": 20},
)
