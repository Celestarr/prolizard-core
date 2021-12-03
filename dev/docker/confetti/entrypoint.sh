#!/bin/bash

python -m venv --clear venv

source venv/bin/activate

python -m pip install --upgrade pip
pip install --requirement requirements.txt

cd app

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init

exec python manage.py runserver 0.0.0.0:9901 "$@"
