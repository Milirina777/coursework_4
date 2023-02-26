from flask_restx import Resource, Namespace

from project.dao.model.director import DirectorSchema
from project.implemented import director_service
from project.services.auth_service import auth_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """Получение всех режиссеров"""
        data = director_service.get_all()
        result = DirectorSchema(many=True).dump(data)
        return result, 200


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    @auth_required
    def get(self, uid):
        """Получение режиссера по id"""
        get_one_director = director_service.get_one(uid)
        schema_of_director = DirectorSchema().dump(get_one_director)
        return schema_of_director, 200
