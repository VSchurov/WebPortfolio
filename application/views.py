from flask import Blueprint, render_template


index = Blueprint('index', __name__, '/')

@index.route('/')
@index.route('/index')
def homepage():
    return render_template('index.html')