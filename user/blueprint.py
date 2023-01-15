from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/')
def index():
    return render_template('user/index.html')


@user.route('/login')
@user.route('/register')
def user_login():
    pass


@user.route('/logout')
def user_logout():
    pass



