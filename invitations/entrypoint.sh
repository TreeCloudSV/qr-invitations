#!/bin/sh
export $(egrep  -v '^#'  /run/secrets/* | xargs)
python manage.py migrate
python manage.py collectstatic --no-input && python manage.py makemigrations && python manage.py migrate && gunicorn --workers=3 invitations.wsgi -b 0.0.0.0:8000

