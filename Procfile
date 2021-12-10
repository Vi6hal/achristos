release: python manage.py migrate
web: gunicorn achristos.wsgi
celery: celery -A achristos worker -l info -c 4