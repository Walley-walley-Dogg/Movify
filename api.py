import requests
from config import KINIPOISK_API_KEY

API_URL = "https://api.kinopoisk.dev/v1.4/movie/random"

def get_random_movie():
    """Запрашивает случайный фильм с API Кинопоиска"""
    headers = {"accept": "application/json", "X-API-KEY": KINIPOISK_API_KEY}
    response = requests.get(API_URL, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data.get("alternativeName", "Без названия"),
            "year": data.get("year", "Неизвестно"),
            "countries": ", ".join([c["name"] for c in data.get("countries", [])]),
            "poster": data.get("poster", {}).get("url", None)
        }
    return None
