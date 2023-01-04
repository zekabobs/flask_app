from app import app
from app import db

from posts.blueprint import posts
import view

from models import Tag
from models import Post
from models import post_tag

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
