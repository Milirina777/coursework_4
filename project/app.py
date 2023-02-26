from flask import Flask, render_template
from flask_cors import CORS
from flask_restx import Api

from config import Config
from project.setup_db import db

from project.views.auth.auth_ import auth_ns
from project.views.main.directors import director_ns
from project.views.main.genres import genre_ns
from project.views.main.movies import movie_ns
from project.views.auth.user import users_ns


def create_app(config_object):
    app = Flask(__name__)
    CORS(app)
    @app.route('/')
    def index():
        return render_template('index.html')

    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app, doc="/docs")
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=25000, debug=True)