from flask import request
from flask_restx import Resource, Namespace

from project.dao.model.movie import MovieSchema
from project.implemented import movie_service
from project.services.auth_service import auth_required

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """Получение всех фильмов или сортировка по фильтрам (статус, страницы)"""
        status = request.args.get("status")
        page = request.args.get("page")
        filters = {
            "status": status,
            "page": page
        }
        all_movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    @auth_required
    def post(self):
        movie = movie_service.create(request.json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    @auth_required
    def get(self, uid):
        """Получение фильма по id"""
        one_movie = movie_service.get_one(uid)
        schema_of_movie = MovieSchema().dump(one_movie)
        return schema_of_movie, 200

    @auth_required
    def put(self, uid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = uid
        movie_service.update(request_json)
        return "Added", 204

    @auth_required
    def delete(self, uid):
        movie_service.delete(uid)
        return "Deleted", 204
