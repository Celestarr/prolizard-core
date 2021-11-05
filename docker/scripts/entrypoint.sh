#!/bin/bash

python -m pip install --user --upgrade pip
pip install --requirement requirements.txt

cd app

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init

exec python manage.py runserver 0.0.0.0:9901 "$@"
