from sqlalchemy import desc

from project.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

    def get_all(self, query):
        return query.all()

    def get_movie(self):
        return self.session.query(Movie)

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def get_new(self, query):
        movies = query.order_by(desc(Movie.year))
        return movies

    def get_page(self, query, limit, offset):
        movies = query.limit(limit).offset(offset)
        return movies
