# Dash `pages` multi-page app demos

This repo contains minimal examples of multi-page apps using the Pages feature available in dash>=2.5.1

__See the :new: Dash Documentation [Multi-Page Apps and URL Support](https://dash.plotly.com/urls)__  

__:movie_camera: Don't miss the video tutorials:__
 - [Introducing Dash `pages` --  A better way to make multi-page apps`](https://youtu.be/pJMZ0r84Rqs) by Adam Schroeder and Chris Parmer.  
 - Charming Data Videos by Adam Schroeder:
      - [Creating Multi Page Apps - Part I ](https://youtu.be/Hc9_-ncr4nU) Getting Started
      - [Creating Multi Page Apps - Part II](https://www.youtube.com/watch?v=MtSgh6FOL7I) Sidebar and Layout Enhancements


This feature was developed in dash-labs.  For background, see the thread on the [Dash Community Forum.](https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview/57775/)

I hope these examples help you get started exploring all the cool features in Pages. If you find this project helpful, please consider giving it a :star:

---------------------------

__Example Apps__

The best way to get started is to clone this repo and run the examples locally.  See a brief description of each app below.

__Other tutorials or examples using `pages`:__  


1. Adding a Blog to your Dash app.  See  this [Dash Community Forum post](https://community.plotly.com/t/adding-a-blog-to-your-dash-app/65955). It describes how to do this and includes [this repo](https://github.com/bradley-erickson/dash-blog-page) from @bradley-erickson. 

2. See the [Dash Webb Compare](https://dash-webb-compare.herokuapp.com/ ) app live.  This app shows the first images from the James Webb Space Telescope. Compare before and after images of Hubble vs Webb. The Github repo has 2 versions of the app using `pages`.  
    - [app_pages.py](https://github.com/AnnMarieW/webb-compare/blob/master/app_pages.py) - Creates an multi-page app without using the `pages` folder.
    - [app_pages_no_assets.py](https://github.com/AnnMarieW/webb-compare/blob/master/app_pages_no_assets.py) - This multi-page app uses images that are hosted on GitHub so it doesn't use either the `pages` or the `assets` folder.  
   
__Tips and Tricks__
1. [Pretty print dash.page_registry](#1-print_registry-from-dash-labs-110) - with the `print_registry()` function from dash-labs
2. [How to use dcc.Link in Markdown](#2-tada-use-dcclink-in-dccmarkdown)  - for high performance page navigation from a link in a dcc.Markdown component.
3. [Avoiding duplicate ids](#3-avoiding-duplicate-ids) - Strategies for handling ids in a large multi-page app.
4. [Display loading screen when page_container is loading](https://community.plotly.com/t/displaying-loading-screen-when-pages-container-is-loading/72109/1) - Shows how to make the overall loading screen only display when there is a change to the `_pages_content` that involves a layout being changed and not changes within the layout.

---


<br>
<br>

# Example Apps
## 1. [multi_page_basics/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_basics)

This folder has a minimal overview of the basic `pages features`, including:
- setting the default home page
- handling variables in the pathname
- updating the app title and description with a function
- handling variable in query strings
- setting redirects
- adding extra data to the `dash.page_registry`
- customizing the `dash.page_registry` defaults
- how images are added to meta tags
- adding pages without using the pages folder

The image below :point_down: is from the `path_variables` page.  Note that asset "inventory" and department "branch-1001" are passed from the pathname to the layout function and are displayed on the page.

![basics](https://user-images.githubusercontent.com/72614349/174487978-ceaac40c-4421-4d86-b9a4-077a7cf85d3d.png)

----


<br>
<br>

## 2. [multi_page_pathname_prefix/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_basics_pathname_prefix)
    
This example shows how to use the `relative_path` attribute in `dash.page_registry` in deployment environments that use a pathname prefix.
It also shows use of `dash.get_asset_url()` to get the correct path to the `assets` folder from a file in the `pages` folder.

- `relative_path`:
        The path with `requests_pathname_prefix` prefixed before it.
        Use this path when specifying local URL paths that will work
        in environments regardless of what `requests_pathname_prefix` is.
        In some deployment environments, like Dash Enterprise,
        `requests_pathname_prefix` is set to the application name,
        e.g. `my-dash-app`.
        When working locally, `requests_pathname_prefix` might be unset and
        so a relative URL like `/page-2` can just be `/page-2`.
        However, when the app is deployed to a URL like `/my-dash-app`, then
        `relative_path` will be `/my-dash-app/page-2`.


__Note the `/app1/` pathname prefix in the url__ :point_down: 

![pathname_prefix](https://user-images.githubusercontent.com/72614349/174487979-4e9a4d6f-bad4-45b3-bef7-db59ae04a84d.png)

-------


<br>
<br>

## 3. [multi_page_cache/]()

Example removed - please see  #11 multi_page_store and #4 multi_page_cach_background_callbacks.


---

<br>




## 4. [multi_page_cache_background_callbacks](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_cache_background_callback)
This example shows how to use caching and background callbacks in a multi-page app.  The examples in the dash docs needed to be modified to make it possible to switch pages 
while background callbacks are running.  



<br>
<br>

## 5. [multi_page_example1/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_example1)

This example shows a small app with three pages with callbacks.  Each page displays a figure.  It uses dash-bootstrap-components with `dbc.DropdownMenu` to display the links in a navbar.

## 5a. [multi_page_dash_auth](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_dash_auth)
This example is the `multi_page_example1` app with `HTTP Basic Auth from the `dash-auth` package.
[Basic Auth](https://dash.plotly.com/authentication#basic-auth) section of the dash docs.

![Example1](https://user-images.githubusercontent.com/72614349/174487976-57f797b7-c2e5-4ab6-8f05-0cc62e176898.png)


---
<br>
<br>

## 6. [multi_page_flask_login/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_flask_login)

You will find two similar examples.    

  1.  [multi_page_flask_login/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_flask_login) - original example  
  2.  [multi_page_flask_login2/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_flask_login2) - the new and improved version contributed by @jinnyzor.  See this [Dash Community Forum](https://community.plotly.com/t/dash-app-pages-with-flask-login-flow-using-flask/69507) post for more information


__For other authentication options see:__
  - [Dash Enterprise Auth](https://dash.plotly.com/authentication#dash-enterprise-auth)
 - [Dash Basic Auth](https://dash.plotly.com/authentication#basic-auth)


![flask__login](https://user-images.githubusercontent.com/72614349/174487970-74351830-b971-4874-bb3f-d33d2fdec74c.gif)

-----


<br>
<br>

## 7. [multi_page_layout_functions/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_layout_functions)
This app demonstrates how to create a sub-topics sidebar that is only used in certain pages.  It shows how to use
functions to access the `dash.page_registry` from within the `pages` folder after it's finished building. 
For more details see the dash docs: https://dash.plotly.com/urls#dash-page-registry

It also shows how arbitrary data added to the `dash_page_registry` can be used.  In this app, we add `top_nav=True` on the
three pages we want to include in the top nav bar.  Then we create the nav links like this:

```python
    dbc.Nav(
        [
            dbc.NavLink(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page.get("top_nav")
        ],
    ),
```

![pages-side-nav-funct](https://github.com/AnnMarieW/dash-multi-page-app-demos/assets/72614349/ca6bd011-57e3-4c5f-b72a-c64a97437f70)

---

<br>
<br>

## 7b [multi_page_path_variables](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_path_variables)

Here's how to make an example like the one above, but using path variables.  
This example also shows how to add a different title and meta tag descriptions for each of the pages specified in the path variable.

For more information, see this forum post on how to [Contain a Dash Page Under a Parent Page.](https://community.plotly.com/t/contain-a-dash-page-under-a-parent-page/82695/)


![multi-page-demo-path-variables](https://github.com/AnnMarieW/dash-multi-page-app-demos/assets/72614349/1ef50a6d-32ac-4fe5-9fcd-ef83b5e77558)


---

<br>
<br>

## 8. [multi_page_meta_tags/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_meta_tags)

This app shows more details on how the images are added to the meta tags.
See also the Dash Documentation:  https://dash.plotly.com/urls#meta-tags

---

<br>
<br>

## 9. [multi_page_nested_folder/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_nested_folders)

For more info, please see the Dash Documentation:  https://dash.plotly.com/urls#nested-pages
This app demonstrates the case where you have nested folders with pages folder, like in the following:
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


It also demos how to add arbitrary data to the `page_registry`.  It adds icons to the `page_registry` which are used when creating the links.

This app uses  [dash-mantine-components](https://dash-mantine-components.herokuapp.com/dash-iconify) and [dash-iconify libraries.](https://dash-mantine-components.herokuapp.com/dash-iconify)
![nested_folders](https://user-images.githubusercontent.com/72614349/175791749-4c6aafc2-b49e-403f-b651-9b24bdce565a.png)

------


<br>
<br>

## 10. [multi_page_query_strings/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_query_strings)

This app demonstrates passing variables to a page using query strings.
For more information see the Dash Documentation:  https://dash.plotly.com/urls#query-strings.
You will also see how to use a `dcc.Link` within a `dcc.Markdown`

![query_strings](https://user-images.githubusercontent.com/72614349/175389777-dbf10ccf-d4cb-4f86-9e09-12a7ad048fd5.gif)

----


<br>
<br>

## 11. [multi_page_store/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_store)
This app shows how to share data between callbacks on different pages using a `dcc.Store` component.

![pages-share-data-between-pages](https://github.com/AnnMarieW/dash-multi-page-app-demos/assets/72614349/80473cef-3dc8-4d66-821f-095cfe09a25b)

----


<br>
<br>

## 12. [multi_page_table_links/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_table_links)

This app uses  `dcc.Link`in the cells of a Dash AG Grid  to navigate to a new page without refreshing the page. 

![grid links](https://github.com/AnnMarieW/dash-multi-page-app-demos/assets/72614349/123d0abf-d0f3-4a5c-ae8f-2b6dbc7c9d1c)



----


<br>
<br>

## 13. [multi_page_sync_components/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_sync_components)

These examples show how to synchronize component values between pages. 

You will find two example:  

 1. [multi_page_sync_components/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_sync_components) is a simple example which uses the same component on each page and sets `persistence=True`  Thanks @nopria for the example!
 2. [multi_page_sync_components2/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_sync_components2)In some cases, the simple example won't work (ie component values updated in callbacks).  Version 2 uses a `dcc.Store` component to sync the component values.  It required dash>=2.9.2 to allow updating the dcc.Store from multiple callbacks on different pages.

![sync](https://user-images.githubusercontent.com/72614349/175389756-bf064f6d-edd1-4107-9764-1373c260451f.gif)

---


<br>
<br>

## 14. [multi_page_theme_switch/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_theme_switch)
This example demonstrate a light and dark theme switch component from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
See a live demo at [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/)  The Theme Explorer app is also made with `pages` :tada:


__For Dash Enterprise Customers, see: [Dash Design Kit](https://plotly.com/dash/design-kit/)__



![theme_switch](https://user-images.githubusercontent.com/72614349/174487972-078fec10-a54f-418d-b0c4-8de0e8e4b438.gif)



------


<br>
<br>

## Navigation in a callback

With Dash Pages, the routing callback is under-the-hood, which reduces the amount of boilderplate code you need to write.
The best way to navigate is to use components such as the `dcc.Link` or `dbc.Button`. When the user clicks on these
links, it will navigate to the new page without refreshing the page, making the navigation very
fast.  And the best part?  No callback required! :tada:

This works well when you have static links. However, at times, you may want to navigate based on an input field,
dropdown, or clicking on a figure etc. There are two options:

1) Update href of `dcc.Location` in a callback. Not recommended in Dash<2.9.2 because it refreshes the page.
2) Update the link in a callback.  Best practice!

:tada:  New in dash 2.9.2  `dcc.Location(refresh="callback-nav")`  - navigate without refreshing the page.  See examples below

---

<br>
<br>

### 15. [multi_page_update_url_in_callback/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_update_url_in_callback)
### 15b.[multi_page_update_url_in_callback_V292/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_update_url_in_callback_V292)

See two versions of the same app. It shows both ways to navigate in a callback - by updating dcc.Location and by updating links.
The V2.9.2 version uses the "callback-nav" option in `dcc.Location` so that the page does not refresh.


![callback-nav](https://user-images.githubusercontent.com/72614349/230732368-f9d48477-92ef-4d73-a099-227bcaa7871f.png)


For more information see this [community forum post.]()

Here are more examples.  This one (best practice) is to update a link when a user clicks on a figure:

---
<br>
<br>

### 16. [multi_page_update_url_from_figure/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_update_url_from_figure)

![fight-status](https://user-images.githubusercontent.com/72614349/187049002-6ae8fc65-c9f7-4f4b-b823-538301391792.gif)


---
<br>
<br>

### 16b. [multi_page_update_url_from_figure_V292/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_update_url_from_figure_V292)

This option is available with dash>=2.9.2.  It uses `dcc.Location(refresh="callback-nav")` to navigate without refreshing the page.
  img

![callback-nav-fig-292](https://user-images.githubusercontent.com/72614349/230731674-81ff311a-fbd4-4770-aae3-bc587c0ad2c9.gif)


There are some known issues with `dcc.Location`.  Here are some workarounds to avoid things like the browser crashing or the back button not
working: 
- Only include a `dcc.Location` component if you need to update it in a callback.
- Be sure to use only one `dcc.Location` component - do not use multiple.
- Place the `dcc.Location` in `app.py` - do not put it in a file in the `pages` folder.
- Place the `dcc.Location` component as the first component in the `app.py` layout. It must be in the layout before `page_container` which has the Pages `dcc.Location` component.

```python

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh="callback-nav"),
        navbar, page_container,
    ], 
)

```


---



<br>
<br>

# Tips and Tricks

## 1. print_registry() from dash-labs>-1.1.0



When debugging a `pages` app, it's very helpful to inspect the content of the  `dash.page_registry`.  

`print_registry()` is a handy utility that pretty-prints all or part of the `dash.page_registry` dict.


Examples for `print_registry()`


```


from dash import Dash, html, register_page

# must use dash-labs>=1.1.0
from dash_labs import print_registry

app = Dash(__name__, use_pages=True)

register_page("another_home", layout=html.Div("We're home!"), path="/")

print_registry()

.... rest of your app

```
Will print to the console:

```
{'another_home': {'module': 'another_home',
                  'supplied_path': '/',
                  'path_template': None,
                  'path': '/',
                  'supplied_name': None,
                  'name': 'Another home',
                  'supplied_title': None,
                  'title': 'Another home',
                  'description': '',
                  'order': 0,
                  'supplied_order': None,
                  'supplied_layout': Div("We're home!"),
                  'image': None,
                  'supplied_image': None,
                  'image_url': None,
                  'redirect_from': None,
                  'layout': Div("We're home!")}}
```

__Reference__

`print_registry(modules='ALL', exclude=None, include='ALL')`
   
Params:
- `module`: (string or list) Default "ALL".  Specifies which modules to print.
-  `exclude`: (string or list) Default None.   Specifies which of the page's  parameter(s) to exclude.
 - `include`: (string or list) Default "ALL".  Prints only the parameters that are specified.
 
Examples:
 
  - `print_registry()`  Will print the entire content of dash.page_registry. If called from a file in the pages folder `dash.page_registry` may not be complete.
   - `print_registry("pages.home")` will print only one module, in this case, the `pages.home` module
   - `print_registry(__name__)`  will print the current module.  When called from app.py it will print all modules.   
   - `print_registry(["pages.home", "pages.archive"])` Will print the modules in the list.
   - `print_registry(exclude="layout")`  will print info for all the modules, but will exclude the "layout" attribute
   - `print_registry(include=["path", "name"]` will print only the "path" and "name" attributes for all modules   
   - `print_registry(include=None)` prints the keys (module names) only

------------------


<br>
<br>

## 2. :tada: Use dcc.Link in dcc.Markdown

Did you know it's possible to use dcc.Link in  `dcc.Markdown`?
The advantage of using  `dcc.Link` to navigate between pages of a multi-page app is that when you click on the link it updates the pathname without refreshing the page --  which makes browsing really fast. :rocket:

Here's how:
```python
dcc.Markdown( "This is text <dccLink href='page1/news' children='Page 1' /> more text", dangerously_allow_html=True)
```

For comparison, here is a regular Markdown link syntax:
```python
dcc.Markdown( "This is text [Page 1](/page1/news) more text")
```
See [multi_page_query_strings/](#9-multi_page_query_strings) for an example.
For more examples including how to format the link title with Markdown syntax or use an image [get the gist.](https://gist.github.com/AnnMarieW/b5269c177cc3dfed06766aded802f664)


<br>
<br>

## 3. Avoiding duplicate ids

All ids in the entire app must be unique, otherwise callbacks may not fire.   Here are some tips to ensure that all ids in the app are unique:

__3a. From this [forum post](https://community.plotly.com/t/examples-of-multi-page-apps-with-dash-pages/66489/8?u=annmariew) as recommended by @chriddyp:__

>What I’ve done in big projects is to create an id function that creates the prefix automatically. This is easier with pages as each component tree is in its own layout so you can use `__name__` as the prefix.  
> 
> So you’d write something like:

`utils.py`
```
def id(name, localid):
    return f"{name.replace('_', '-').replace('.py', '').replace('/', '')}-{localid}"
```

`pages/historical_analysis.py`
```
from utils import id

layout = html.Div(id=id(__name__, 'parent-div'))
```

__3b. From this [video by arjancodes ](https://youtu.be/XOFrvzWFM7Y)__

Define ids in module.  It makes them easier to access, maintain, and reduces typos.
See this used in [multi_page_long_callback](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_long_callback) 

for example:

`ids.py`
```
PAGE1_BUTTON = "page1-button"
PAGE1_GRAPH = "page1-graph"
```
`page1.py`
```python
import ids

html.Button("button", id=ids.PAGE1_BUTTON)
dcc.Graph(ids.PAGE1.GRAPH)

@callback(
    Output(ids.PAGE1_GRAPH, "figure"),
    Input(ids.PAGE1_BUTTON, "n_clicks")
)


```


<br>
<br>

## 4. Display loading screen when page_container is loading
Shows how to make the overall loading screen only display when there is a change to the `_pages_content` that involves a layout being changed and not changes within the layout.  See the post on the [Dash Community Forum](https://community.plotly.com/t/displaying-loading-screen-when-pages-container-is-loading/72109/1).  Thanks @BSd3v for this example!

