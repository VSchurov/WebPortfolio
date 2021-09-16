import os
from pathlib import Path

from flask import Flask

def create_app():
    app = Flask(__name__)

    myfile=Path('sqlite:///application/test.db')
    try:
        myfile.exists()
    finally:
        from application.db.engine import Session
    return app
