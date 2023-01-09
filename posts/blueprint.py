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


@posts.route('/<slug>/edit', methods=['GET', 'POST'])
def edit_post(slug):
    editing_post = Post.query.filter(Post.slug == slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=editing_post)
        form.populate_obj(editing_post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=editing_post.slug))

    form = PostForm(title=editing_post.title, body=editing_post.body, created=editing_post.created)
    form.created.render_kw = {'disabled': 'disabled'}
    return render_template('posts/edit_post.html', form=form, post=editing_post)


@posts.route('/')
def index():
    q = request.args.get('q', '')
    page = request.args.get('page', '')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if q:
        all_posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        all_posts = Post.query.order_by(Post.created.desc())

    pages = all_posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', posts=all_posts, pages=pages)


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
