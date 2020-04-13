#!/bin/sh
export FLASK_APP=login_service.py
. venv/bin/activate
pip install -r requirements.txt
flask run --port=5000

