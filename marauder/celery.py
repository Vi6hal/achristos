from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','marauder.settings')

app = Celery('marauder')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks()
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test_periodic.s('hello \n\n\n'), name='add every 10')

@app.task
def test_periodic(arg):
    print(arg)