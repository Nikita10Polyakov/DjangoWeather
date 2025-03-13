from django.urls import path
from .views import WeatherDataList, WeatherDataByCity, update_weather_api

urlpatterns = [
    path('weather/', WeatherDataList.as_view(), name='weather-api'),  
    path('weather/<str:city>/', WeatherDataByCity.as_view(), name='weather-api-city'),  
    path('update/', update_weather_api, name='update-weather-api'),  
]
