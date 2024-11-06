#!/bin/sh
set -e

python manage.py collectstatic --noinput

echo 'Executando makemigrations'
python manage.py makemigrations --noinput

echo 'Executando migrate'
python manage.py migrate --noinput

if [ "$LOCALHOST" = "True" ]; then
    echo 'Run Server'
    python manage.py runserver 0.0.0.0:8100
else
    echo 'Gunicorn'
    gunicorn project.wsgi:application --bind 0.0.0.0:8100 --worker-class gevent --timeout 600
fi