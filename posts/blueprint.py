from flask import Blueprint
from flask import render_template, redirect

from flask import request
from flask import url_for

from models import Post
from models import Tag

from .forms import PostForm

from app import db, app


posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create', methods=['GET', 'POST'])
def create_post():
    alert = False
    if request.method == 'POST':
        title = request.form['title'].strip()
        body = request.form['body'].strip()

        try:
            new_post = Post(title=title, body=body)
            with app.app_context():
                db.session.add(new_post)
                db.session.commit()
        except:
            alert = True
        else:
            return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form, alert=alert)


@posts.route('/')
def index():
    q = request.args.get('q', '')
    if q:
        all_posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        all_posts = Post.query.order_by(Post.created.desc())
    return render_template('posts/index.html', posts=all_posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts_tag = tag.posts
    return render_template('posts/tag_detail.html', tag=tag, posts=posts_tag)
