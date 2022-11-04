from dash import dcc

years = tuple(range(2010, 2023))

app_spanning_input = dcc.Dropdown(
    options=years,
    id="all-pages-year",
    persistence=True,
    persistence_type = 'memory',
)