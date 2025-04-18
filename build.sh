#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectionstatic --noinput
python manage.py migrate
