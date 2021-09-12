from flask import Blueprint, render_template, request


class ApplicationBlueprints:
    bpv_projects = Blueprint('projects', __name__, template_folder="application/templates")
    bpv_index = Blueprint('index', __name__, template_folder="application/templates")

    # defining projects page url as `http://app/projects/{project}
    # GET method if project exist, POST if you wanna add project
    @bpv_projects.route('/')
    @bpv_projects.route('/{project}/', methods=('GET', 'POST'))
    def projects(self, project):
        if request.method == 'GET':
            try:
                return render_template(f'/projects/{project}')  # Format this string to flexible
            finally:
                pass
        else:
            pass  # TODO: create project panel

    @bpv_index.route('/')
    @bpv_index.route('/index/')
    def index(self):
        try:
            return render_template('index')
        finally:
            return render_template('issues/some_fixes')  # TODO: make tech issues page
