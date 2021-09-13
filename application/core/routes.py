import os

from flask import Blueprint, render_template, current_app

from application.core.exceptions.exceptions import PageNotFoundError
from application.templates import url_dict

template_dir = os.path.abspath('../templates')


class ApplicationBlueprints:
    bpv_projects = Blueprint('projects', __name__, cli_group='other', template_folder=template_dir)
    bpv_index = Blueprint('index', __name__, cli_group='other')

    # defining projects page url as `http://app/projects/{project}
    # GET method if project exist, POST if you wanna add project
    @bpv_projects.route('/projects/')
    @bpv_projects.route('/projects/<project_id>/')
    def projects(self, project_id=1):
        try:
            return render_template(current_app.config["projects.html"])
        except PageNotFoundError:
            raise render_template(current_app.config['errors/404.html'])
        # if request.method == 'GET':
        #     try:
        #         return render_template(f'/projects/{project_id}')  # Format this string to flexible
        #     finally:
        #         pass
        # else:
        #     return  # TODO: create project panel

    @bpv_index.route('/')
    @bpv_index.route('/index/')
    def index(self):
        try:
            return render_template(current_app.config['index'])
        finally:
            return render_template(current_app.config['issues/some_fixes'])  # TODO: make tech issues page
