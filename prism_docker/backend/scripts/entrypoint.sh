#!/bin/sh

python3 -m venv /opt/venv
/opt/venv/bin/pip install --upgrade pip
/opt/venv/bin/pip install -r /backend/requirements.txt
sh /wait-for-db.sh

export PYTHONIOENCODING=utf8
/opt/venv/bin/python manage.py runserver 0.0.0.0:8000