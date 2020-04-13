from flask import Flask, redirect, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from base_converter import base_converter as base
from base64 import urlsafe_b64encode as b64encode
from base64 import urlsafe_b64decode as b64decode
import sqlite3

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-top-secret'
jwt = JWTManager(app)

host = 'http://localhost:5001/'
db_urls = 'databases/urls.db'

def setup_database_session():
    db = sqlite3.connect(db_urls, check_same_thread=False)
    return db.cursor()

cursor = setup_database_session()

@app.route('/<string:value>', methods=['GET'])
def single_action_get(value):
    res = cursor.execute('SELECT URL FROM WEB_URL WHERE ID=(?)', 
        (base.toBase10(value),)).fetchall()
    if len(res) == 0:
        return '404 Not Found', 404
    shortened_url = host + value
    full_url = str(b64decode(res[0][0])).strip("'b").strip("'")
    return 'The full URL from ' + shortened_url + ' is: ' + full_url, 301

@app.route('/<string:value>', methods=['POST'])
@jwt_required
def single_action_post(value):
    url = str.encode(value)
    res = cursor.execute('INSERT INTO WEB_URL (URL) VALUES (?)', 
        [b64encode(url)])
    encoded_string = base.toBase62(res.lastrowid)
    return 'The shortened URL from ' + value + ' is: ' + host + encoded_string, 201

@app.route('/<string:value>', methods=['PUT'])
@jwt_required
def single_action_put(value):
    new_url = 'www.put.com'
    url = str.encode(new_url)
    res = cursor.execute('SELECT URL FROM WEB_URL WHERE ID=(?)', 
        (base.toBase10(value),)).fetchall()
    if len(res) == 0:
        return '404 Not Found', 404
    res = cursor.execute('UPDATE WEB_URL SET URL = ? WHERE ID = ?', 
        (b64encode(url), base.toBase10(value))).fetchall()
    return 'The full URL for ' + host + value + ' is now: ' + new_url, 200

@app.route('/', methods=['PUT'])
@jwt_required
def single_action_put2():
    return '400 Server Error', 400

@app.route('/<string:value>', methods=['DELETE'])
@jwt_required
def single_action_delete(value):
    res = cursor.execute('SELECT ID FROM WEB_URL WHERE ID=(?)', 
        (base.toBase10(value),)).fetchall()
    if len(res) == 0: 
        return '404 Not Found', 404
    res = cursor.execute('DELETE FROM WEB_URL WHERE ID=(?)', 
        (base.toBase10(value),))
    return 'Entry with key: ' + value + ' has been deleted', 202

@app.route('/', methods=['GET'])
@jwt_required
def bulk_action_get():
    res = cursor.execute('SELECT ID FROM WEB_URL',).fetchall()
    key_list = []
    for key in res:
        key_list.append(base.toBase62(key[0]))
    return 'Available keys:\n\n' + str(key_list), 200

@app.route('/', methods=['DELETE'])
@jwt_required
def bulk_action_delete():
    res = cursor.execute('DELETE FROM WEB_URL',)
    return 'The database has been cleared', 204
