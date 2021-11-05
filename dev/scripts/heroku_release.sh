#!/usr/bin/env bash

python manage.py migrate
python manage.py loaddata user_management-dev.json oauth2_provider-dev.json
exit 0
