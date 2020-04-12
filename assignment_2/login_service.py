from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['json']
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)
logins = {'shane': 'secret'} # temporary

@app.route('/users/', methods=['POST'])
def create_user():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == '' or password == '':
        return 'Expected parameters are: username, password', 403
    elif username in logins:
        return 'Username already exists', 403

    logins[username] = password
    return 'New user "' + username + '" created', 200

@app.route('/users/login/', methods=['POST'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username not in logins or logins.get(username) != password:
        return 'Invalid credentials', 403

    access_token = create_access_token(identity=username)
    return 'Login success\nAccess token = ' + access_token, 200
