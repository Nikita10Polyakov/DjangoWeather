from django.urls import path
from .views import weather_view, update_weather_api, WeatherDataList, WeatherDataByCity

urlpatterns = [
    path('', weather_view, name='weather'),
    path('api/weather/', WeatherDataList.as_view(), name='weather-api'),  
    path('api/weather/<str:city>/', WeatherDataByCity.as_view(), name='weather-api-city'),  
    path('api/update/', update_weather_api, name='update-weather-api'),  
]
