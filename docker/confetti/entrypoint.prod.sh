#!/bin/bash

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init

exec gunicorn wsgi \
    --config /etc/gunicorn.conf.py \
    --name mortred \
    --log-level=debug \
    "$@"
