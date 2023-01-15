from flask import Blueprint
from flask import render_template
from flask import redirect

from flask_security import (
    login_user,
    logout_user,
    user_registered,
    AnonymousUser
)

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/')
def index():
    return render_template('user/index.html')


@user.route('/login')
def user_login():
    return render_template('user/index.html')


@user.route('/logoutA')
def user_logout():
    pass


@user.route('/reset')
def user_reset():
    pass
