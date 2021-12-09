release: python manage.py migrate
web: gunicorn marauder.wsgi
celery: celery -A marauder worker -l info -c 4
celery-beat: celery -A marauder beat -l info