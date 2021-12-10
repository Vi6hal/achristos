from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','achristos.settings')

app = Celery('achristos')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()