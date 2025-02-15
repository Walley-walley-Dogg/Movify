import requests
from config import KINIPOISK_API_KEY

API_URL = "https://api.kinopoisk.dev/v1.4/movie/random"

def get_random_movie():
    headers = {"accept": "application/json", "X-API-KEY": KINIPOISK_API_KEY}
    response = requests.get(API_URL, headers=headers)
    
 
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Проверяем, нет ли ошибки HTTP (например, 401, 403, 500 и т. д.)
        data = response.json()  # Преобразуем JSON в словарь
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None
    except ValueError:
        print("Ошибка: получен некорректный JSON")
        return None

    if not data:
        return None

    # Формируем строку рейтингов: выводим все ключи, значения которых не равны 0
    raw_ratings = data.get("rating", {})
    filtered_ratings = {k: v for k, v in raw_ratings.items() if v != 0}
    ratings_str = ", ".join(f"{k.upper()}: {v}" for k, v in filtered_ratings.items()) if filtered_ratings else "Нет данных"

    return {
        "title": data.get("alternativeName", "Без названия"),
        "year": data.get("year", "Неизвестно"),
        "countries": ", ".join([country["name"] for country in data.get("countries", [])]) or "Не указана",
        "poster": data.get("poster", {}).get("url"),
        "genres": ", ".join([genre["name"] for genre in data.get("genres", [])]) or "Не указан",
        "ratings": ratings_str,
        "ageRating": data.get("ageRating", "Не указан")
    }