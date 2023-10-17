import datetime
import sqlite3

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = 1;"
SELECT_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"

connection = sqlite3.connect("data.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIE, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor
        if upcoming:
            timestamp = datetime.datetime.today().timestamps()
            cursor.execute(SELECT_UPCOMING_MOVIES, (timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movie(movie_title):
    with connection:
        connection.execute(SELECT_WATCHED_MOVIES, (movie_title,))


def get_watched_movies(movie_title):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (movie_title,))
        return cursor