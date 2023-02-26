from project.dao.director import DirectorDAO

class DirectorsService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, uid):
        """Отображает режиссёра по id"""
        return self.dao.get_one(uid)

    def get_all(self):
        """Отображает всех режиссёров"""
        return self.dao.get_all()

    def create(self, director_new):
        return self.dao.create(director_new)

    def update(self, director_info):
        self.dao.update(director_info)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)
