#!/bin/bash

source ../venv/bin/activate

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init

exec gunicorn confetti.wsgi \
    --config /etc/gunicorn.conf.py \
    --name confetti \
    --log-level=debug \
    "$@"
