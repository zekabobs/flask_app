from flask import Blueprint
from flask import render_template
from flask import request

from models import Post
from models import Tag
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/create')
def create_post():
    form = PostForm()
    return render_template('posts/create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q', '')
    if q:
        all_posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        all_posts = Post.query.all()
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
