from project.dao.user import UserDAO
from project.services.auth_service import get_hash, password_check


class UsersService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, new_user):
        """Создаем пользователя в системе"""
        new_user["password"] = get_hash(new_user.get("password"))
        return self.dao.create(new_user)

    def update(self, user_info):
        self.dao.update(user_info)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def password_update(self, user_data):
        user_email = user_data.get("email")
        user_info = self.dao.get_by_email(user_email)

        password_old = user_data.get("password_1")
        password_new_hash = get_hash(user_data.get("password_2"))

        if user_info is None:
            return "User is not exist!", 403
        elif not password_check(password_old, user_info.password):
            return "Password is incorrect", 403

        user = self.dao.password_update(user_info, password_new_hash)

        return user
