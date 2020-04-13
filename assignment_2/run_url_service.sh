#!/bin/sh
export FLASK_APP=url_shortener_service.py
. venv/bin/activate
pip install -r requirements.txt
flask run --port=5001

