from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/<string:value>', methods=['GET','POST','PUT','DELETE'])
def single_action_handler(value):
    if request.method == 'POST':
        # TODO shorten the url
        # return 201 with id, or 400 with "error"
        return 'post: ' + value
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
