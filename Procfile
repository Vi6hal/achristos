release: python manage.py migrate
web: gunicorn achristos.wsgi
celery: celery -A achristos worker -l info -c 4
celery-beat: celery -A achristos beat -l info