from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy

ckeditor = CKEditor()

db = SQLAlchemy()

DB_NAME = "posts.db"


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    ckeditor.init_app(app)

    app.config['SECRET_KEY'] = "this is some secret stuff"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app
