#!/bin/sh
export $(egrep  -v '^#'  /run/secrets/* | xargs)
python manage.py migrate
python manage.py collectstatic  --no-input
gunicorn invitations.wsgi:application --bind 0.0.0.0:8000 --workers 3

