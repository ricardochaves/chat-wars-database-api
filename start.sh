#!/bin/bash

export $(egrep -v '^#' .env | xargs)


python manage.py makemigrations
python manage.py migrate
python manage.py superuserseed
python manage.py seeddb

python manage.py runserver ${HOST}:${PORT}
