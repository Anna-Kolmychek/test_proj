#!/bin/env
echo "Making migrations..."
python manage.py makemigrations
echo "Running migrations..."
python manage.py migrate
#echo "Importing test data..."
#python manage.py import_test_data


mkdir -p /app/backend_static
echo "Collect static files..."
python manage.py collectstatic --noinput
echo "Copy static files..."
cp -r /app/staticfiles/. /app/backend_static/

# Start gunicorn and daphne
echo "Starting gunicorn..."
gunicorn --bind 0.0.0.0:9000 --workers 3 config.wsgi:application 0
exec "$@"
