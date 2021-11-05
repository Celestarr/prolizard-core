#!/bin/bash

# Try upgrading pip
python -m pip install --user --upgrade pip

# Install dependencies
pip install --requirement requirements.txt

# Change directory
cd app

# Run pending database migrations
python manage.py migrate

# Compile message files
python manage.py compilemessages

# Compile message files
python manage.py collectstatic --noinput

# Start the server
exec python manage.py runserver 0.0.0.0:9901 "$@"
