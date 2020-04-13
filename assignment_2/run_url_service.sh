#!/bin/sh
export FLASK_APP=url_shortener_service.py
source $(. )venv/bin/activate
flask run --port=5001

