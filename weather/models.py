from django.db import models
from django.utils import timezone


class WeatherData(models.Model):
    city = models.CharField(max_length=255, unique=True) 
    temperature = models.FloatField()
    humidity = models.IntegerField()
    weather_description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.city} - {self.temperature}°C, {self.weather_description}"
