"""
Example of managing ids in a large multi page app
 Option 1 use the `id` function to create a unique id based on the module name
 Option 2 define the ids as constants.

"""


def id(name, localid):
    """
    Creates a unique id by adding the module name as a prefix to the local ids.
    Converts the module name to an id
    Usage:  `layout = html.Div(id=id(__name__, 'parent-div'))`

    :param name: Prefix for the local id to ensure id is unique in the entire app.
    :param localid: the local id - must be unique within the module
    :return: a unique string id
    """
    return f"{name.replace('_', '-').replace('.py', '').replace('/', '')}-{localid}"


EXAMPLE_1_P = "example-1-p"
EXAMPLE_1_BUTTON = "example-1-button"


EXAMPLE_2_P = "example-2-p"
EXAMPLE_2_BUTTON = "example-2-button"


EXAMPLE_3_P = "example-3-p"
EXAMPLE_3_BUTTON = "example-3-button"
EXAMPLE_3_CANCEL = "example-3-cancel"


EXAMPLE_4_P = "example-4-p"
EXAMPLE_4_BUTTON = "example-4-button"
EXAMPLE_4_CANCEL = "example-4-cancel"
EXAMPLE_4_PROGRESS_BAR = "example-4-progress-bar"


EXAMPLE_5_P = "example-5-p"
EXAMPLE_5_BUTTON = "example-5-button"
EXAMPLE_5_CANCEL = "example-5-cancel"
EXAMPLE_5_PROGRESS_BAR_GRAPH = "example-5-progress-bar"
