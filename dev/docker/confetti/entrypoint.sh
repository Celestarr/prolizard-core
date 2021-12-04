#!/bin/bash

python -m pip install --upgrade pip
pip install --requirement requirements.txt

cd app

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init
python manage.py create_superuser --email "su@myfolab.com" --password "suadmin"

exec python manage.py runserver 0.0.0.0:9901 "$@"
