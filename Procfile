release: python manage.py migrate
web: gunicorn pacemaker.wsgi
celery: celery -A pacemaker worker -l info -c 4
celery-beat: celery -A pacemaker beat -l info