import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER,
    movie_id INTEGER,
    movie_title TEXT,
    movie_year TEXT,
    movie_country TEXT,
    movie_poster TEXT,
    movie_genres TEXT,
    movie_ratings TEXT
)
""")


conn.commit()

def add_favorite(user_id, movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings):
    cursor.execute("""
        INSERT INTO favorites (user_id, movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings))
    conn.commit()


def get_favorites(user_id):
    cursor.execute("SELECT movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings FROM favorites WHERE user_id = ?", (user_id,))
    return cursor.fetchall()