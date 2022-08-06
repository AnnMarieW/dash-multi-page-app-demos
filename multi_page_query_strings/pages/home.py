from dash import dcc, html
import dash

dash.register_page(__name__, path="/")

text = """
__This is a demo of how to use query strings to pass variables to other pages of a multi-page app.__

See the bar chart page with tips on:
  - <dccLink children="Saturday" href="/bar-chart?day=Sat" />
  - <dccLink children="Sunday" href="/bar-chart?day=Sun" />
  
--------------
 
__This app also demos how to use high performance `dcc.Link` within  `dcc.Markdown`__

One of the great things about multi-page apps with Dash is that the when you navigate with `dcc.Location`
 and `dcc.Link`, it will update the layout without refreshing the page, making the navigation super fast.
 
The links above are high performance dcc.Link components. They are defined in the Markup text like this:
```
<dccLink children="Saturday" href="/bar-chart?day=Sat"/>
```

Here's the same link with the standard Markdown format `[Saturday](/bar-chart?day=Sat)`
Give it a try!  This simple page updates pretty fast, but you will notice a brief flash while the page updates:

 - [Saturday](/bar-chart?day=Sat)

For more information, see this [Dash Community Forum post](https://community.plotly.com/t/how-to-use-dcc-link-in-dcc-markdown-for-high-performance-links/66781).


----------

Of course, you can also use `dcc.Link` with query strings in your layout in the standard way:
```python
html.Div([
    dcc.Link("Saturday", href="/bar-chart?day=Sat")
    ...
])
```

"""

layout = dcc.Markdown(text, dangerously_allow_html= True, style={"margin": 50})
