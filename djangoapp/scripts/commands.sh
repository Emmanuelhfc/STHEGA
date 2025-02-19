#!/bin/sh
set -e
python manage.py collectstatic --noinput

if [ "$PRODUCTION" = "0" ]; then
    echo 'Executando makemigrations'
    python manage.py makemigrations --noinput
fi

echo 'Executando migrate'
python manage.py migrate --noinput

if [ "$PRODUCTION" = "1" ]; then
    echo 'Gunicorn'
    gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers 3 
else
    echo 'Run Server'
    python manage.py runserver 0.0.0.0:8000
fi
