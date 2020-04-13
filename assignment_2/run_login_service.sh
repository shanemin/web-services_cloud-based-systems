#!/bin/sh
export FLASK_APP=login_service.py
source $(. ) venv/bin/activate
flask run --port=5000

