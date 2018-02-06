#!/bin/sh
pipenv run python3.6 manage.py createdb
pipenv run python3.6 manage.py migrate
pipenv run python3.6 manage.py fixtures user team_catalogue team performance score

# Run test cases
pipenv run python3.6 manage.py test

# Run server
pipenv run python3.6 manage.py runserver 0.0.0.0:8000
