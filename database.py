import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS favorites (
    user_id INTEGER,
    movie_id INTEGER UNIQUE,
    movie_title TEXT,
    movie_year TEXT,
    movie_country TEXT,
    movie_poster TEXT,
    movie_genres TEXT,
    movie_ratings TEXT
)
""")
conn.commit()

def add_favorite(user_id, movie):
   
    try:
        cursor.execute("""
            INSERT INTO favorites 
            (user_id, movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            movie["id"],
            movie["title"],
            movie["year"],
            movie["countries"],
            movie["poster"],
            movie["genres"],
            str(movie["rating"])  
        ))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Ошибка: Фильм '{movie['title']}' уже в избранном у пользователя {user_id}.")
        return False
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False

def get_favorites(user_id):
    
    try:
        cursor.execute("""
            SELECT movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings 
            FROM favorites WHERE user_id = ?
        """, (user_id,))
        movies = cursor.fetchall()
        return movies if movies else None
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return None

def get_random_favorite(user_id):
    
    try:
        cursor.execute("""
            SELECT movie_id, movie_title, movie_year, movie_country, movie_poster, movie_genres, movie_ratings 
            FROM favorites WHERE user_id = ? ORDER BY RANDOM() LIMIT 1
        """, (user_id,))
        movie = cursor.fetchone()
        return movie if movie else None
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return None

def remove_favorite(user_id, movie_id):
    
    try:
        cursor.execute("DELETE FROM favorites WHERE user_id = ? AND movie_id = ?", (user_id, movie_id))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Ошибка базы данных: {e}")
        return False