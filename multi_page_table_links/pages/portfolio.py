"""
Example of using links in a DataTable to navigate to another page.

"""
from dash import dash_table, dcc, html, register_page
import pandas as pd
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

# Create dataframe
equities = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Alphabet": "GOOGL",
    "Berkshire Hathaway": "BRK.B",
    "Johnson & Johnson": "JNJ",
}

data = {
    "Equities": [f"[{stock}](/stocks/{ticker})" for stock, ticker in equities.items()],
    "Quantity": [75, 40, 100, 5, 40, 60],
    "Market Price": [131.55, 247.39, 105.80, 2143.50, 268.08, 169.85],
    "Market Value": [9866.25, 9895.60, 10580.00, 10717.50, 10723.2, 10191.00],
}

df = pd.DataFrame(data)

# dash.DataTable with links formatted by setting the column to  "presentation": "markdown"
datatable = dash_table.DataTable(
    data=df.to_dict("records"),
    columns=[{"id": "Equities", "name": "Equities", "presentation": "markdown"}]
    + [{"id": c, "name": c} for c in df.columns if c != "Equities"],
    markdown_options={"link_target": "_self"},
    css=[{"selector": "p", "rule": "margin: 0"}],
    style_cell={"textAlign": "right"},
)


# html table with links formatted using dcc.Link()
df["Equities"] = [
    dcc.Link(f"{stock}", href=f"/stocks/{ticker}") for stock, ticker in equities.items()
]
table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

layout = html.Div(
    [
        html.H5(
            "html table with dcc.Link  Note:  No page refresh on navigation",
            className="mt-5",
        ),
        table,
        html.H5(
            "DataTable with Markdown links", className="mt-5"
        ),
        datatable,
    ]
)
