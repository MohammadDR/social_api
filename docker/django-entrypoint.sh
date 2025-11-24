#!/bin/sh

# Wait for DB to be ready (optional)
# e.g., for Postgres: sleep 10

# Apply migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn social_api.wsgi:application --bind 0.0.0.0:8000
