from flask import Flask, request, render_template, redirect
from math import floor
from sqlite3 import OperationalError
from urllib.parse import urlparse
import string
import sqlite3
import base64


app = Flask(__name__)
host = 'http://localhost:5000/'
str_encode = str.encode

def table_check():
    create_table = """
        CREATE TABLE WEB_URL(
        ID INT PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError:
            pass


def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits+string.ascii_letters
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

@app.route('/<string:value>', methods=['GET','POST','PUT','DELETE'])
def single_action_handler(value):
    if request.method == 'POST':
        original_url = str_encode(request.form.get('url'))
        if urlparse(original_url).scheme == '':
            url = 'http://' + original_url
        else:
            url = original_url
        with sqlite3.connect('urls.db') as conn:
            cursor = conn.cursor()
            res = cursor.execute(
                'INSERT INTO WEB_URL (URL) VALUES (?)',
                [base64.urlsafe_b64encode(url)]
            )
            encoded_string = toBase62(res.lastrowid)
        return 'post: ' + render_template('home.html', short_url=host + encoded_string)
        # TODO shorten the url
        # return 201 with id, or 400 with "error"
    if request.method == 'GET':
        # TODO get full address from id (?)
        # return 301 with value, or 404
        return 'get: ' + value
    if request.method == 'PUT':
        # TODO 
        # return 200, 400 with "error", or 404
        return 'put: ' + value
    if request.method == 'DELETE':
        # TODO delete the key/values
        # return 202 or 404
        return 'delete: ' + value


@app.route('/', methods=['GET','DELETE'])
def bulk_action_handler():
    if request.method == 'GET':
        # TODO get all stored keys (or empty)
        # return 200 with keys
        return 'get all'
    if request.method == 'DELETE':
        # TODO delete all stored keys/values
        # return 204
        return 'delete all'
