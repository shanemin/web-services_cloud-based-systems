#!/bin/sh
export FLASK_APP=url_shortener_service.py
source $(. )venv/bin/activate
pip3 install -r requirements.txt
flask run --port=5001

