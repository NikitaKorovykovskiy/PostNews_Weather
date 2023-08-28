import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab
from django.conf import settings as s

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("proj")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Настройка периодических задач
    app.conf.beat_schedule = {
        # # Задача для получения погодных данных
        # "fetch_weather_data": {
        #     "task": "weather.tasks.fetch_weather_data",
        #     "schedule": timedelta(hours=1),
        # },
        # Задача для отправки новостных email
        "send_email": {
            "task": "posts.tasks.send_email",
            "schedule": crontab(
                hour=s.CONFIG.EMAIL_SEND_TIME.hour,
                minute=s.CONFIG.EMAIL_SEND_TIME.minute,
            ),
        },
    }
