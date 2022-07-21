# Dash `pages` multi-page app demos

This repo contains minimal examples of multi-page apps using the `pages` feature available in dash>=2.5.1

__See the Dash Documentation :new: [Multi-Page Apps and URL Support](https://dash.plotly.com/urls)__  

This feature was developed in dash-labs.  For background, see the thread on the [Dash Community Forum.](https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview/57775/)
If you have a multi-page app using the `pages` plugin from dash-labs, see the post on [how to migrate to dash>=2.5.1.](https://community.plotly.com/t/introducing-dash-pages-a-dash-2-x-feature-preview/57775/132?u=annmariew) 


__Demos__

The examples are listed by their folder name.
 1. [multi_page_basics/](#1-multi_page_basics) - minimal overview of basic pages features.
 2. [multi_page_pathname_prefix/](#2-multi_page_pathname_prefix) - overview using a pathname prefix.
 3. [multi_page_cache/](#3-multi_page_cache) - sharing data between pages with caching.
 4. [multi_page_example1/](#4-multi_page_example1) - 3 page app with header navbar, graphs and callbacks.  Uses [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/).
 5. [multi_page_flask_login/](#5-multi_page_flask_login) - uses flask-login to secure one page of a multi-page app.
 6. [multi_page_layout_functions/](#6-multi_page_layout_functions) - uses a function to access `dash.page_registry` from within the pages folder to build a sidebar.
 7. [multi_page_meta_tags/](#7-multi_page_meta_tags) - how images are used in meta tags when sharing the app on social media.
 8. [multi_page_nested_folder/](#8-multi_page_nested_folder) - creates a sidebar from a sub folder in the pages folder and adds arbitrary data to `dash.page_registry`. Uses [dash-mantine-components](https://www.dash-mantine-components.com/)
 9. [multi_page_query_strings/](#9-multi_page_query_strings) - passes variables to the layout function from the url query string.
 10. [multi_page_store/](#10-multi_page_store) - sharing data between pages with a `dcc.Store`.
 11. [multi_page_table_links/](#11-multi_page_table_links) - uses links in a DataTable and an html table for navigation and passes variables from the pathname to the page layout function.
 12. [multi_page_sync_components/](#12-multi_page_sync_components) - syncs components between pages using MultiplexerTransform from dash-extensions to update a dcc.Store from multiple callbacks.
 13. [multi_page_theme_switch/](#13-multi_page_theme_switch) - demos a light and dark theme switch component from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.
 14. [multi_page_update_url_in_callback/](#14-multi_page_update_url_in_callback) - page navigation via callback rather than a user clicking on a link.

__Tips and Tricks__
1. [Pretty print dash.page_registry](#1-print_registry-from-dash-labs-110) - with the `print_registry()` function from dash-labs
2. [How to use dcc.Link in Markdown](#2-tada-use-dcclink-in-dccmarkdown)  - for high performance page navigation from a link in a dcc.Markdown component.

--------
---------

# Demos
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
## 3. [multi_page_cache/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_cache)

This example shows how to share data between pages of a multi-page app using caching.

The easiest way to share data between callbacks is to use dcc.Store(). See also example #10 multi-page-store. However, if you have large data, then you may want to use caching as described in example 3 and 4 in the Dash tutorial [sharing data between callbacks.](https://dash.plotly.com/sharing-data-between-callbacks)

This example also demonstrates the use of the new `dash.get_app()` function that can be used to access the `app` object from modules within the `pages` folder without running into the circular imports issue. 
![cache](https://user-images.githubusercontent.com/72614349/174487969-92fda7eb-9b9f-4797-8648-dc4809e31feb.png)

---------
## 4. [multi_page_example1/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_example1)

This example shows a small app with three pages with callbacks.  Each page displays a figure.  It uses dash-bootstrap-components with `dbc.DropdownMenu` to display the links in a navbar.


![Example1](https://user-images.githubusercontent.com/72614349/174487976-57f797b7-c2e5-4ab6-8f05-0cc62e176898.png)

## 5. [multi_page_flask_login/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_flask_login)

This shows a minimal example of `flask-login` to secure one of the pages of a multi-page app.
This code is adapted for `pages`  based on Nader Elshehabi's  [article](https://dev.to/naderelshehabi/securing-plotly-dash-using-flask-login-4ia2) and [github](https://github.com/naderelshehabi/dash-flask-login) repo.

__For other authentication options see:__
  - [Dash Enterprise Auth](https://dash.plotly.com/authentication#dash-enterprise-auth)
 - [Dash Basic Auth](https://dash.plotly.com/authentication#basic-auth)


![flask__login](https://user-images.githubusercontent.com/72614349/174487970-74351830-b971-4874-bb3f-d33d2fdec74c.gif)

-----
## 6. [multi_page_layout_functions/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_layout_functions)
This app demonstrates how to create a sub-topics sidebar that is only used in certain pages.  It shows how to use functions to access the `dash.page_registry` from within the `pages` folder after it's finished building.
For more details see also: https://dash.plotly.com/urls#dash-page-registry

## 7. [multi_page_meta_tags/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_meta_tags)

This app shows more details on how the images are added to the meta tags.
See also the Dash Documentation:  https://dash.plotly.com/urls#meta-tags

## 8. [multi_page_nested_folder/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_nested_folders)

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
 This app also demos how to add arbitrary data to the `page_registry`.  This example adds icons to the `page_registry` which are used when creating the links.

![nested_folders](https://user-images.githubusercontent.com/72614349/175791749-4c6aafc2-b49e-403f-b651-9b24bdce565a.png)

------
## 9. [multi_page_query_strings/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_query_strings)

This app demonstrates passing variables to a page using query strings.
For more information see the Dash Documentation:  https://dash.plotly.com/urls#query-strings

![query_strings](https://user-images.githubusercontent.com/72614349/175389777-dbf10ccf-d4cb-4f86-9e09-12a7ad048fd5.gif)

----

## 10. [multi_page_store/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_store)
This app shows how to share data between callbacks on different pages using a `dcc.Store` component.

![share_data_between_pages](https://user-images.githubusercontent.com/72614349/175132278-ef8a5098-9c05-4e2d-a00e-e8fac73bd743.gif)

-----
----------

## 11. [multi_page_table_links/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_table_links)

This app uses links in a table to navigate to a different page. 
It shows two tables:
- The `dash.DataTable` has links formatted using Markdown.
- The html table uses `dcc.Link`.  The advantage of the html table is `dcc.Link` allow for the navigation to a new page without refreshing the page. The table is created with the `dbc.Table.from_dataframe` function from the `dash-bootstrap-components` library.  

![table_links](https://user-images.githubusercontent.com/72614349/175389810-fc60beed-9684-4ca8-96fa-d7c5e765e93a.gif)


----

## 12 [multi_page_sync_components/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_sync_components)

This example shows how to synchronize component values between pages. It uses [MultiplexerTransform from the dash-extensions](https://www.dash-extensions.com/transforms/multiplexer-transform) library to update a `dcc.Store` component from multiple callbacks.

![sync](https://user-images.githubusercontent.com/72614349/175389756-bf064f6d-edd1-4107-9764-1373c260451f.gif)
---

## 13. [multi_page_theme_switch/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_theme_switch)
This example demonstrate a light and dark theme switch component from the [dash-bootstrap-templates](https://github.com/AnnMarieW/dash-bootstrap-templates) library.

![theme_switch](https://user-images.githubusercontent.com/72614349/174487972-078fec10-a54f-418d-b0c4-8de0e8e4b438.gif)

------

## 14. [multi_page_update_url_in_callback/](https://github.com/AnnMarieW/dash-multi-page-app-demos/tree/main/multi_page_update_url_in_callback)

This example shows how to update the url in a callback. It passes the value of the dcc.Input to the layout of a different page as a path variable.
It also demonstrates using `urllib.parse.unquote` to get decoded strings from the url.  

![update_url_in_callback](https://user-images.githubusercontent.com/72614349/174862799-e08cf136-15da-4831-9415-4faee2984729.gif)  


---
---

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

For more examples including how to format the link title with Markdown syntax or use an image [get the gist.](https://gist.github.com/AnnMarieW/b5269c177cc3dfed06766aded802f664)