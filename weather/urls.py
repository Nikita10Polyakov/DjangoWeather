from django.urls import path
from .views import weather_view, update_weather_api, WeatherDataList, WeatherDataByCity

urlpatterns = [
    # Головна сторінка з погодою
    path('', weather_view, name='weather'),

    # API маршрути
    path('api/weather/', WeatherDataList.as_view(), name='weather-api'),  # Всі записи погоди
    path('api/weather/<str:city>/', WeatherDataByCity.as_view(), name='weather-api-city'),  # Погода для конкретного міста
    path('api/update/', update_weather_api, name='update-weather-api'),  # Оновлення погоди через API
]
