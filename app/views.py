from flask import Flask, render_template
from flask import Blueprint
from .models import Post
from . import db


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


@views.route("/about")
def about():
    return render_template('about.html')


@views.route("/contact")
def contact():
    return render_template("contact.html")
