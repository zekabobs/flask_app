from flask import Blueprint
from flask import render_template


user = Blueprint('users', __name__, template_folder='templates')


@user.route('/')
def index():
    return '<h1>Unreleased yet</h1>'