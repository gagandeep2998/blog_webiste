from flask import Flask, render_template, redirect, url_for
from flask import Blueprint
from .models import Post
from . import db
from .forms import CreatePostForm
from datetime import date

views = Blueprint("views", __name__)


@views.route("/")
def home():
    all_posts = Post.query.all()
    print(all_posts)
    return render_template("index.html", posts=all_posts)


@views.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = Post.query.get(post_id)
    return render_template("post.html", post=requested_post)


@views.route("/new-post", methods=["POST", "GET"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = Post(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template('make-post.html', form=form)


@views.route("/about")
def about():
    return render_template('about.html')


@views.route("/contact")
def contact():
    return render_template("contact.html")
