import hashlib
import hmac
import calendar
import datetime

import jwt
from flask import request
from flask_restx import abort

from project.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM, PWD_ALGO
from project.dao.auth import AuthDAO



def generate_jwt(token_data):
    # 30 минут жизни для access_token
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    token_data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(token_data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    # 60 дней жизни для refresh_token
    days60 = datetime.datetime.utcnow() + datetime.timedelta(days=60)
    token_data["exp"] = calendar.timegm(days60.timetuple())
    refresh_token = jwt.encode(token_data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

def password_check(password_to_check, password_hash):
    password_to_check_coded = hashlib.pbkdf2_hmac(
        PWD_ALGO,
        password_to_check.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS).decode("utf-8", "ignore")

    return hmac.compare_digest(password_to_check_coded.encode('utf-8'), password_hash.encode('utf-8'))


def get_hash(password):
    return hashlib.pbkdf2_hmac(
        PWD_ALGO,
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ).decode("utf-8", "ignore")


def check_token(token):
    try:
        token_data = jwt.decode(token.get('refresh_token'), JWT_SECRET, algorithms=JWT_ALGORITHM)
        return token_data
    except Exception as e:
        print("Decoding error", e)
        return False


def auth_required(func):
    def wrappers(*args, **kwargs):
        data = request.headers
        if 'Authorization' not in data:
            abort(401)
        token_data = data.get('Authorization')

        token = token_data.split('Bearer ')[-1]

        try:
            jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
            return func(*args, **kwargs)
        except Exception as e:
            print("Authorisation error", e)
            abort(401)
    return wrappers


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def get_token(self, user_data):
        user_email = user_data.get("email")
        user_info = self.dao.get_by_user(user_email)

        if user_info is None:
            return "User is not exist!", 403
        elif not password_check(user_data.get("password"), user_info.password):
            return "Password is incorrect", 403

        token_data = generate_jwt(user_data)
        return token_data
