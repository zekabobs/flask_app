from app import app
from app import db

from posts.blueprint import posts
from user.blueprint import user

import view

app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(user, url_prefix='/users')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
