# Weather Dashboard

## Overview

This is a Django-based web application that collects, processes, and displays weather data from a public API. It demonstrates proficiency in Python, Django, PostgreSQL, Celery, Redis, and frontend development.

The dashboard provides real-time weather updates for multiple cities worldwide, utilizing asynchronous task scheduling for data updates and a RESTful API for external access.

## Features 

### Core Functionality

Fetches weather data for 5 major cities from OpenWeather API

Stores weather data in a PostgreSQL database

Automated updates using Celery & Redis

RESTful API to access weather data

Dashboard with real-time weather conditions and visualizations

### Technical Stack 🛠

Backend: Django, Django REST Framework

Database: PostgreSQL

Task Queue: Celery + Redis

Frontend: HTML, CSS, JavaScript (Chart.js)

API Integration: OpenWeatherMap

# Installation & Setup

## Clone the repository

git clone https://github.com/Nikita10Polyakov/DjangoWeather

cd weather-dashboard

## Set up a virtual environment

python -m venv venv

source venv/bin/activate  (On macOS/Linux)

venv\Scripts\activate    (On Windows)

## Install dependencies

pip install -r requirements.txt

## Set up environment variables

Create a .env file and add your OpenWeather API key:

OPENWEATHER_API_KEY=your_api_key_here

## Apply database migrations

python manage.py migrate

## Run Redis (Ensure Redis is installed and running)

redis-server  (On macOS/Linux)

redis-server.exe  (On Windows - if installed manually)

## Start Celery workers

celery -A weather_dashboard worker --loglevel=info --pool=solo

## Run Celery Beat (For periodic weather updates)

celery -A weather_dashboard beat --loglevel=info

## Start the Django server

python manage.py runserver

Now, open your browser and go to http://127.0.0.1:8000/weather/ 

# API Documentation 

The application provides a RESTful API to access weather data:

## Get all weather data

GET /api/weather/

#### Response:

[
  {"city": "London", "temperature": 10.5, "humidity": 80, "weather_description": "Cloudy"},
  {"city": "Paris", "temperature": 12.3, "humidity": 75, "weather_description": "Sunny"}
]

## Get weather data for a specific city

GET /api/weather/{city}/

#### Example:

GET /api/weather/London/

#### Response:

{"city": "London", "temperature": 10.5, "humidity": 80, "weather_description": "Cloudy"}

## Manually trigger weather update

POST /api/update/

#### Response:

{"message": "Weather update initiated."}

## Developed by Mykyta Poliakov
