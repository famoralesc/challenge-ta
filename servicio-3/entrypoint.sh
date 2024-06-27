#!/bin/bash

set -e

cd "./challenge"

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8080
