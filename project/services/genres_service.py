from project.dao.genre import GenreDAO


class GenresService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, uid):
        """Отображает жанр по id"""
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()
