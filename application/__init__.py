import os

from flask import Flask
# from werkzeug.serving import run_simple

from application.core import get_blueprints_list
from application.core.exceptions import FileExistException

#   This function probably not necessary cause appending to a list of functions done earlier
# def register_blueprints_in_app():
#     bp = get_blueprints_list()
#     list_blueprints = []
#     bpv_projects = bp.projects()
#     list_blueprints.append(bpv_projects)
#     bpv_index = bp.index()
#     list_blueprints.append(bpv_index)
#     return list_blueprints


def create_app():
    # This is factory to create one instance of application
    app = Flask(__name__)
    app.config.from_pyfile("config/config.py")

    # Maybe this check isn't that needed
    #
    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except (FileExistException) as fee:
    #     raise FileExistException("need to clean this shit", fee, fee.args)

    bp_list = get_blueprints_list()

    for item in bp_list:
        app.register_blueprint(item)

    return app


def run_flask():
    app = create_app()
    return app
