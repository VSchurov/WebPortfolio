"""

following the oficial (and non-oficial too) guides we put all factories into isolated module.
IDK  actually needless of main app. But maybe we can solve at least one problem
functions that (will) be represented here:

`def create_app` : application factory. Hided from application/__init__.py file
`def register_blueprints` :

"""
from flask import Flask

from application.core import get_blueprints_list
from application.core.exceptions import FileExistException
from application.config.jinja import (env as jinja_conf,  # do not use name 'jinja_env' cause it exist in flask
                                      MyLoader)

def create_app(config_filename):
    app = Flask(__name__)

    # Some app configuration variables. Can be changed later
    app.c

    blueprints_list = get_blueprints_list()
