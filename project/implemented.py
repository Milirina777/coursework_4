from project.dao.movie import MovieDAO
from project.dao.user import UserDAO
from project.dao.genre import GenreDAO
from project.dao.director import DirectorDAO
from project.dao.auth import AuthDAO

from project.services.directors_service import DirectorsService
from project.services.genres_service import GenresService
from project.services.movies_service import MoviesService
from project.services.users_service import UsersService
from project.services.auth_service import AuthService

from project.setup_db import db

# DAO
director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)
user_dao = UserDAO(session=db.session)
auth_dao = AuthDAO(session=db.session)

# Services
director_service = DirectorsService(dao=director_dao)
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
auth_service = AuthService(dao=auth_dao)

