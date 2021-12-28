import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flower_shop.settings")

app = Celery("flower_shop")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
