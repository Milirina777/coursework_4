from flask_restx import Resource, Namespace

from project.dao.model.genre import GenreSchema
from project.implemented import genre_service
from project.services.auth_service import auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """Получение всех жанров"""
        return GenreSchema(many=True).dump(genre_service.get_all()), 200


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    @auth_required
    def get(self, uid):
        """Получение жанра по id"""
        return GenreSchema().dump(genre_service.get_one(uid)), 200
