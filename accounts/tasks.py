from __future__ import absolute_import
from celery import shared_task
import requests

@shared_task
def add():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n running task ~~~~~~~~~~~~~~~~~~~~~~~~~")
    # requests.get("https://sobercheck.herokuapp.com/data")
    return