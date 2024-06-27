#!/bin/bash

set -e

./wait-for-it.sh challenge-ta-mysql-1:3306 -t 10

cd "./challenge"

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8080
