from flask import request
from flask_restx import Namespace, Resource

from project.dao.model.user import UserSchema
from project.implemented import user_service

users_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@users_ns.route('/')
class UserView(Resource):
    def get(self):
        """Получаем информацию о пользователе (его профиль)"""
        user = user_service.get_all()
        result = users_schema.dump(user)
        return result, 200

    def patch(self):
        """Изменяем информацию пользователя"""
        user_service.update(request.json)
        return 'Ready!', 201

@users_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        res = user_schema.dump(user)
        return res

    def delete(self, uid):
        user_data = user_service.delete(uid)
        result = user_schema.dump(user_data)
        return result, 'Information is deleted', 204

@users_ns.route('/password/')
class UserPassView(Resource):
    """Обновление пароля пользователя"""
    def put(self):
        user_service.password_update(request.json)
        return 'Ready!', 201
