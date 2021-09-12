import os

from flask import Flask

def create_app(test_config=None):
    # This is factory to create one instance of application
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',   # temporary set to static string. Later it will be credentials
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),  # TODO: change database to postgreSQL
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except:
        pass

    # a simple page to say hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
