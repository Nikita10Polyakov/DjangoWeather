from django.conf import settings
import requests
from django.utils import timezone
from weather.models import WeatherData

# Використовуємо API-ключ із settings.py
API_KEY = settings.OPENWEATHER_API_KEY
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    """Отримує актуальні дані про погоду для заданого міста."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "uk"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print(f"Помилка отримання погоди: {data.get('message', 'Невідома помилка')}")
            return None

        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_description": data["weather"][0]["description"],
            "timestamp": timezone.now(),
        }

        # Використовуємо update_or_create(), щоб уникнути дублювання
        WeatherData.objects.update_or_create(
            city=weather_data["city"],  # Поле для перевірки унікальності
            defaults=weather_data  # Дані для оновлення
        )

        return weather_data

    except requests.RequestException as e:
        print(f"Помилка HTTP-запиту: {e}")
        return None
    except KeyError as e:
        print(f"Помилка обробки JSON-відповіді: Відсутнє поле {e}")
        return None
