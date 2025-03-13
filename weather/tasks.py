from celery import shared_task
from django.utils import timezone
from weather.services import fetch_weather
from weather.models import WeatherData

CITIES = ["London", "New York", "Tokyo", "Paris", "Berlin", "Madrid"]


@shared_task
def update_weather():
    for city in CITIES:
        data = fetch_weather(city)
        if data:
            WeatherData.objects.update_or_create(
                city=data["city"],
                defaults={
                    "temperature": data["temperature"],
                    "description": data.get("weather_description", "No description"),
                    "timestamp": timezone.now(),
                }
            )
    return "Weather updated successfully!"
