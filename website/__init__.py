from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'IMDB.db'
ALGORITHM = 'HS256'
SECRET_KEY = 'thisisasecretkeyandhopeyoucantseeit' \
             'thisisasecretkeyandhopeyoucantseeit' \
             'thisisasecretkeyandhopeyoucantseeit' \
             'thisisasecretkeyandhopeyoucantseeit'


def create_database(app):
    if not path.exists(f'website/{DB_NAME}'):
        db.create_all(app=app)


def initialize_app():
    from .models import Movie
    from .views import views
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')

    create_database(app)

    return app
