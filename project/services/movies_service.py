from project.constants import PWD_LIMIT
from project.dao.movie import MovieDAO


class MoviesService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, uid):
        """Отображает фильм по id"""
        return self.dao.get_one(uid)

    def get_all(self, status, page):
        """Отображает фильмы по фильтрам status и page (если status присутствует и
        имеет значение new — возвращаем записи в отсортированном виде,
        page на страницу будет возвращать по 12 записей"""
        our_movies = self.dao.get_movie()

        if status == "new":
            our_movies = self.dao.get_new(our_movies)

        if page:
            limit = PWD_LIMIT
            offset = (int(page) - 1) * limit
            our_movies = self.dao.get_page(our_movies, limit, offset)

        our_movies = self.dao.get_all(our_movies)

        return our_movies
