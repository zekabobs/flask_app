from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)
