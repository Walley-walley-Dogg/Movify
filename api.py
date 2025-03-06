import requests
from config import KINIPOISK_API_KEY

API_URL = "https://api.kinopoisk.dev/v1.4/movie/random"

def get_random_movie():
    """Получает случайный фильм с API Кинопоиска."""
    headers = {"X-API-KEY": KINIPOISK_API_KEY}
    
    try:
        response = requests.get(API_URL, headers=headers, timeout=5)
        response.raise_for_status()  
        data = response.json()

        if not data or "docs" not in data or not data["docs"]:
            raise ValueError("API вернуло пустой ответ или данные отсутствуют.")
        
        movie = data["docs"][0]
        return {
            "id": movie.get("id", "N/A"),
            "title": movie.get("alternativeName", "Без названия"),
            "year": movie.get("year", "Неизвестно"),
            "countries": ", ".join([c["name"] for c in movie.get("countries", [])]),
            "genres": ", ".join([g["name"] for g in movie.get("genres", [])]),
            "rating": {k: v for k, v in movie.get("rating", {}).items() if v and v > 0},
            "ageRating": movie.get("ageRating", "Не указано"),
            "poster": movie["poster"]["url"] if movie.get("poster") else None
        }

    except requests.exceptions.Timeout:
        print("Ошибка: Превышено время ожидания ответа от API")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None
    except ValueError as e:
        print(f"Ошибка данных API: {e}")
        return None