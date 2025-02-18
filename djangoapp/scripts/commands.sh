#!/bin/sh
set -e
python manage.py collectstatic --noinput

echo 'Executando makemigrations'
python manage.py makemigrations --noinput

echo 'Executando migrate'
python manage.py migrate --noinput

if [ "$PRODUCTION" = "1" ]; then
    echo 'Gunicorn'
    gunicorn project.wsgi:application --bind 0.0.0.0:8100 --workers 1 --threads 8 --timeout 0
else
    echo 'Run Server'
    python manage.py runserver 0.0.0.0:8100
fi

# python manage.py runserver 0.0.0.0:8100PORT --workers 1 --threads 8 --timeout 0 tutorial.wsgi:application