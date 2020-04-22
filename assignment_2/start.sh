#!/bin/sh
. venv/bin/activate
pip install -q -r requirements.txt
python login_service.py & python url_shortener_service.py