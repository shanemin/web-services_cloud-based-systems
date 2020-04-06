from flask import Flask, request, render_template, redirect
from math import floor
from sqlite3 import OperationalError
from urllib.parse import urlparse
import string
import sqlite3
import base64
import sys
import re

app = Flask(__name__)
host = 'http://localhost:5000/'
str_encode = str.encode
db_file = 'urls.db'

def table_check():
    create_table = """
        CREATE TABLE WEB_URL(
        ID INT PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
        );
        """
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(create_table)
        except OperationalError:
            pass

def toBase62(num, b=62):
    if b <= 0 or b > 62:
        return 0
    base = string.digits + string.ascii_letters
    r = num % b
    res = base[r]
    q = floor(num / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res

def toBase10(string, alphabet=(string.digits + string.ascii_letters)):
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
    for char in string:
        if char not in alphabet:
            return None
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num

@app.route('/<string:value>', methods=['GET'])
def single_action_get(value):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'SELECT URL FROM WEB_URL WHERE ID=(?)',
            (toBase10(value),)).fetchall()
        if len(res) == 0:
            return '404 Not Found', 404
    shortened_url = host + value
    full_url = str(base64.urlsafe_b64decode(res[0][0])).strip("'b").strip("'")
    return 'The full URL from: ' + shortened_url + ' is: ' + full_url, 301

@app.route('/<string:value>', methods=['POST'])
def single_action_post(value):
    # TODO add the regex
    url = re.match('some_regex_here', value)

    if url is None:
        return 'Invalid URL. Must be in the format: some_format', 400
    else: url = str.encode(value)

    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'INSERT INTO WEB_URL (URL) VALUES (?)',
            [base64.urlsafe_b64encode(url)])
        encoded_string = toBase62(res.lastrowid)
    return 'The shortened URL from: ' + value + ' is: ' + host + encoded_string, 201

@app.route('/<string:value>', methods=['PUT'])
def single_action_put(value):
    # TODO return 400 with "error", or 404
    url = str.encode('www.put.com')
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'UPDATE WEB_URL SET URL = ? WHERE ID = ?''', 
            (base64.urlsafe_b64encode(url), toBase10(value)))
    return 'The full URL for ' + host + value + ' is now: www.put.com', 200

@app.route('/<string:value>', methods=['DELETE'])
def single_action_delete(value):
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'SELECT ID FROM WEB_URL WHERE ID=(?)',
            (toBase10(value),)).fetchall()
        if len(res) == 0: 
            return '404 Not Found', 404
        res = cursor.execute(
            'DELETE FROM WEB_URL WHERE ID=(?)',
            (toBase10(value),))
    return 'Entry with key: ' + value + ' has been deleted', 202

@app.route('/', methods=['GET'])
def bulk_action_get():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'SELECT ID FROM WEB_URL',).fetchall()
    key_list = []
    for key in res:
        key_list.append(toBase62(key[0]))
    return 'Available keys:\n\n' + str(key_list), 200

@app.route('/', methods=['DELETE'])
def bulk_action_delete():
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()
        res = cursor.execute(
            'DELETE FROM WEB_URL',)
    return 'The database has been cleared', 204
