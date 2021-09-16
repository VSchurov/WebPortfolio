import os
from pathlib import Path
from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    app.config.from_envvar('APPLICATION_SETTINGS')
    myfile = Path('sqlite:///application/test.db')
    try:
        myfile.exists()
    finally:
        from application.db.engine import Session
    from .views import index
    app.register_blueprint(index)
    return app
