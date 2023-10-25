#!/bin/sh

python3 -m venv /opt/venv
/usr/local/bin/pip install --upgrade pip
/usr/local/bin/pip install -r /backend/requirements.txt
sh /wait-for-db.sh

export PYTHONIOENCODING=utf8
cd /backend/
/opt/venv/bin/python manage.py runserver 0.0.0.0:8000