from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)
