#!/bin/bash

wait_for_port() {
    local host=$1
    local port=$2
    echo "Waiting for $host:$port to be reachable..."

    until nc -zv $host $port &>/dev/null; do
        echo "Checking $host:$port..."
        sleep 1
    done

    echo "$host:$port is reachable."
}

python -m pip install --upgrade pip
pip install --requirement requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py compilemessages -i "venv*"

# Define the file that will indicate if the commands have already been run
FLAG_FILE="/project/.first_run_completed"

# Check if the flag file exists
if [ ! -f "$FLAG_FILE" ]; then
    # Wait for the database to be reachable
    wait_for_port $DB_HOST $DB_PORT

    # Run your commands here
    echo "Running first-time setup commands..."

    python manage.py init
    python manage.py create_superuser --email "admin@prolizard.com" --password "Pr0l124rd"

    # Create the flag file to indicate the commands have been run
    touch "$FLAG_FILE"
else
    echo "First-time setup commands have already been run."
fi

# Execute the main container command
exec "$@"
