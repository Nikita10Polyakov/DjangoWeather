import os
from celery import Celery

# Встановлюємо змінну середовища для налаштувань Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_dashboard.settings')

app = Celery('weather_dashboard')

# Завантажуємо конфігурацію Celery із settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматично знаходить завдання у всіх додатках
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
