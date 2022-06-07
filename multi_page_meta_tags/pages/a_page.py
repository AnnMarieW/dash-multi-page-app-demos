import dash

dash.register_page(__name__)


def layout():
    return """    
    This page uses a generic image.  No image is specified and there is no image that matches
    the module name in the assets folder, so it uses `app.jpeg` or `logo.jpeg` if no `app.jpeg` exists.
    
    The title and description are not supplied, so they will be inferred from the module name. In this 
    case it will be "A page".
        """
