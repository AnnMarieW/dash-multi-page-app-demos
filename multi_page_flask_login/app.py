"""
 CREDIT: This code is adapted for `pages`  based on Nader Elshehabi's  article:
   https://dev.to/naderelshehabi/securing-plotly-dash-using-flask-login-4ia2
   https://github.com/naderelshehabi/dash-flask-login

For other Authentication options see:
  Dash Enterprise:  https://dash.plotly.com/authentication#dash-enterprise-auth
  Dash Basic Auth:  https://dash.plotly.com/authentication#basic-auth

"""


import os

from flask import Flask
from flask_login import login_user, LoginManager, UserMixin, logout_user, current_user

import dash
from dash import dcc, html, Input, Output, State


# Exposing the Flask Server to enable configuring it for logging in
server = Flask(__name__)
app = dash.Dash(
    __name__, server=server, use_pages=True, suppress_callback_exceptions=True
)

# Keep this out of source code repository - save in a file or a database
#  passwords should be encrypted
VALID_USERNAME_PASSWORD = {"test": "test", "hello": "world"}


# Updating the Flask Server configuration with Secret Key to encrypt the user session cookie
server.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))

# Login manager object will be used to login / logout users
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = "/login"


class User(UserMixin):
    # User data model. It has to have at least self.id as a minimum
    def __init__(self, username):
        self.id = username


@login_manager.user_loader
def load_user(username):
    """This function loads the user by user id. Typically this looks up the user from a user database.
    We won't be registering or looking up users in this example, since we'll just login using LDAP server.
    So we'll simply return a User object with the passed in username.
    """
    return User(username)


app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dcc.Store(id="login-status", storage_type="session"),
        html.Div(id="user-status-header"),
        html.Hr(),
        dash.page_container,
    ]
)


@app.callback(
    Output("user-status-header", "children"),
    Input("url", "pathname"),
)
def update_authentication_status(path):
    logged_in = current_user.is_authenticated
    if path == "/logout" and logged_in:
        logout_user()
    if logged_in:
        return dcc.Link("logout", href="/logout")
    return dcc.Link("login", href="/login")


@app.callback(
    Output("output-state", "children"),
    Input("login-button", "n_clicks"),
    State("uname-box", "value"),
    State("pwd-box", "value"),
    prevent_initial_call=True,
)
def login_button_click(n_clicks, username, password):
    if n_clicks > 0:
        if VALID_USERNAME_PASSWORD.get(username) is None:
            return "Invalid username"
        if VALID_USERNAME_PASSWORD.get(username) == password:
            login_user(User(username))
            return "Login Successful"
        return "Incorrect  password"


if __name__ == "__main__":
    app.run_server(debug=True)
