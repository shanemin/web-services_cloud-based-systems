from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-top-secret'
jwt = JWTManager(app)

logins = {'shane': 'secret', 'yuxue': 'secret2', 'mansi': 'secret3'}

@app.route('/users/', methods=['POST'])
def create_user():
    username = request.args.get('username')
    password = request.args.get('password')
    if not username:
        return jsonify({'msg': 'Missing username parameter'}), 400
    if not password:
        return jsonify({'msg': 'Missing password parameter'}), 400
    if username in logins:
        return jsonify({'msg': 'Username already exists'}), 400
    logins[username] = password
    return jsonify({'msg': 'User created: {}'.format(username)}), 200

@app.route('/users/login/', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    if logins.get(username) != password:
        return jsonify({'msg': 'Invalid credentials'}), 403
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
