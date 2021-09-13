import os

from flask import Flask
# from werkzeug.serving import run_simple

from application.core import get_blueprints_list
from application.core.exceptions import FileExistException
from application.config.jinja import (env as jinja_conf,  # do not use name 'jinja_env' cause it exist in flask
                                      MyLoader)


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
    app = Flask(__name__,
                template_folder='application/templates',
                )
    app.config.from_pyfile("config/config.py")

    # both objects is not callable
    # app.jinja_loader(MyLoader)
    # app.jinja_env(jinja_conf)
    # ! Creating jinja environment from application instance overriding existing config !
    # app.create_global_jinja_loader(MyLoader)
    # app.create_jinja_environment(jinja_env)
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

    def reverse_filter(s):
        return s[::-1]

    app.jinja_env.filters['reverse'] = reverse_filter

    return app


# ignition = create_app()
