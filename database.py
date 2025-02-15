import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER,
    movie_title TEXT
)
""")
conn.commit()

def add_favorite(user_id, movie_title):
    """Добавить фильм в избранное"""
    cursor.execute("INSERT INTO favorites (user_id, movie_title) VALUES (?, ?)", (user_id, movie_title))
    conn.commit()

def get_favorites(user_id):
    """Получить список избранных фильмов"""
    cursor.execute("SELECT movie_title FROM favorites WHERE user_id = ?", (user_id,))
    return cursor.fetchall()