web: python manage.py collectstatic --noinput; gunicorn umail.wsgi --workers=4 --bind=0.0.0.0:$PORT umail/settings.py 
