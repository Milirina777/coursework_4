from flask import request
from flask_restx import Namespace, Resource

from project.implemented import auth_service, user_service
from project.services.auth_service import check_token, generate_jwt


auth_ns = Namespace('auth')

@auth_ns.route('/register/')
class AuthUserRegisterView(Resource):
    def post(self):
        """Регистрация нового пользователя"""
        user = user_service.create(request.json)
        return "Вы зарегистрированы", 201, {"new_user": f"/user/{user.id}"}


@auth_ns.route('/login/')
class AuthUserLoginView(Resource):

    def post(self):
        """Авторизация пользователя"""
        return auth_service.get_token(request.json), 201

    def put(self):
        """Обновляем токен"""
        token_ = check_token(request.json)
        if not token_:
            return "Error", 403
        return generate_jwt(token_), 204


