#!/bin/bash

APP_DIR="/home/ubuntu/django-app"
VENV_DIR="venv"
PORT="8000"
LOG_FILE="django.log"

cd $APP_DIR || exit 1

source $VENV_DIR/bin/activate

# Stop old Django process
pkill -f "manage.py runserver" || true

# Run migrations
python manage.py migrate --noinput

# Start Django
nohup python manage.py runserver 0.0.0.0:$PORT > $LOG_FILE 2>&1 &
