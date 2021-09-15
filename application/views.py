from flask import Blueprint, render_template, json


index = Blueprint('index', __name__, '/')


@index.route('/')
@index.route('/index')
def homepage():
    return render_template('index.html')


@index.route('/about')
def about_me():
    return render_template('about_me.html')
