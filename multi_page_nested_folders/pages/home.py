from dash import dcc, register_page
import dash_mantine_components as dmc

register_page(__name__, path="/", icon="fa-solid:home")

layout = dmc.Container(
    [
        dmc.Title("Welcome to the home page"),
        dcc.Markdown(
            """
            This is a demo of a multi-page app with nested folders in the `pages` folder.  
            
            For example:            
            ```
            - app.py 
            - pages
                - chapter1                  
                   |-- page1.py
                   |-- page2.py
                - chapter2                   
                   |-- page1.py
                   |-- page2.py    
                - home.py        
            ```
                        
            This app also demos how to add arbitrary data to the `page_registry`.  This example adds icons to the `page_registry`
            
            ```
            dash.register_page(__name__, icon="fa:bar-chart")
            
            ```
            
            In `app.py` we loop through `dash.page_registry` to create the links:
            
            ```
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter2")
                    ],
            ``` 
            
            """
        ),
    ]
)
