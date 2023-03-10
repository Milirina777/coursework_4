from project.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_user_by_name(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.name = user_d.get("name")
        user.surname = user_d.get("surname")
        user.favorite_genre = user_d.get("favorite_genre")

        self.session.add(user)
        self.session.commit()

    def password_update(self, user_db, password_new_hash):
        user_db.password = password_new_hash

        self.session.add(user_db)
        self.session.commit()

        return user_db

    def get_by_email(self, user_email):
        user_data = self.session.query(User).filter(User.email == user_email).first()
        return user_data
