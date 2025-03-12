from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import WeatherData
from .serializers import WeatherDataSerializer
from .tasks import update_weather
import json

# Головна сторінка з погодою
def weather_view(request):
    latest_weather = WeatherData.objects.order_by('-timestamp').first()
    return render(request, "weather/weather.html", {"weather": latest_weather})

# Оновлення погоди через API
@csrf_exempt
def update_weather_api(request):
    if request.method == "POST":
        update_weather.delay()
        return JsonResponse({"message": "Оновлення погоди запущено."}, status=202)
    return JsonResponse({"error": "Метод не дозволений"}, status=405)

# API для отримання всієї погоди
class WeatherDataList(APIView):
    def get(self, request):
        weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)

# API для отримання погоди по конкретному місту
class WeatherDataByCity(APIView):
    def get(self, request, city):
        try:
            latest_weather = WeatherData.objects.filter(city=city).order_by('-timestamp').first()
            history = WeatherData.objects.filter(city=city).order_by('-timestamp')[:5]

            if not latest_weather:
                return Response({"error": "Дані відсутні"}, status=status.HTTP_404_NOT_FOUND)

            response_data = {
                "city": latest_weather.city,
                "temperature": latest_weather.temperature,
                "humidity": latest_weather.humidity,
                "weather_description": latest_weather.weather_description,
                "timestamp": latest_weather.timestamp,
                "history": [
                    {
                        "timestamp": entry.timestamp,
                        "temperature": entry.temperature
                    } for entry in history
                ]
            }
            return Response(response_data)

        except ObjectDoesNotExist:
            return Response({"error": "Місто не знайдено"}, status=status.HTTP_404_NOT_FOUND)
