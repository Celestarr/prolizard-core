#!/usr/bin/env bash

echo "from user_management.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
exit 0
