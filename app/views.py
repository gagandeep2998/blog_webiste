from flask import Flask, render_template
from flask import Blueprint


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/about")
def about():
    return render_template('about.html')


@views.route("/contact")
def contact():
    return render_template("contact.html")