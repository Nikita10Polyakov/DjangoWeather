from django.contrib import admin
from django.urls import path, include
from weather.views import weather_view, update_weather_api, WeatherDataList, WeatherDataByCity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),  # Головна сторінка з погодою
    path('api/weather/', WeatherDataList.as_view(), name='weather-api'),  # API для всіх записів погоди
    path('api/weather/<str:city>/', WeatherDataByCity.as_view(), name='weather-api-city'),  # API для конкретного міста
    path('api/update/', update_weather_api, name='update-weather-api'),  # API для ручного оновлення погоди
]
