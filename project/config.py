import base64


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAYS = 60

    PWD_HASH_SALT = base64.b64decode("salt")
    PWD_HASH_ITERATIONS = 100_000
    ALGO = 'HS256'

    RESTX_JSON = {
        'ensure_ascii': False,
    }


