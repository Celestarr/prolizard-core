#!/bin/bash

python -m pip install --upgrade pip
pip install --requirement requirements.txt

python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
python manage.py init
python manage.py create_superuser --email "admin@myfolab.com" --password "myfo1234"

exec "$@"
