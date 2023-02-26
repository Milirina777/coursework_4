from project.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Director).get(uid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_new):
        return self.session.create(director_new)

    def update(self, director_info):
        self.session.update(director_info)
        return self.session

    def delete(self, uid):
        self.session.delete(uid)
