from flask import Blueprint, render_template, request

from application.config.jinja import MyLoader
from application.core.exceptions.exceptions import PageNotFoundError


class ApplicationBlueprints:

    bpv_projects = Blueprint('projects', __name__, cli_group='other', template_folder='templates')
    bpv_index = Blueprint('index', __name__, cli_group='other', template_folder='templates')

    # defining projects page url as `http://app/projects/{project}
    # GET method if project exist, POST if you wanna add project
    @bpv_projects.route('/projects/')
    @bpv_projects.route('/projects/1/')
    def projects(self, project_id=1):
        try:
            return render_template('projects/index')
        except PageNotFoundError:
            raise render_template('error/404')
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
            return render_template('index')
        finally:
            return render_template('issues/some_fixes')  # TODO: make tech issues page


