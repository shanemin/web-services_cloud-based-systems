# Assignment 2: RESTful Microservices Architectures

The following has been tested using RHEL 8.1, Python 3.6.8, and Postman 7.21.2 for Linux

## This project uses the _Flask_ and _Flask JWT Extended_ libraries for Python 3.6. Postman is used to test the services. More information can be found here:
- https://flask.palletsprojects.com/en/1.1.x
- https://flask-jwt-extended.readthedocs.io/en/stable
- https://www.postman.com/

## 1. Starting the microservices:
### The easy way:
- In the _assignment2/_ directory, open a new terminal and type `./start.sh`

### The not-so-easy way:
- In the _assignment2/_ directory, open a new terminal and type `. venv/bin/activate` to start the virtual environment
- Type `export FLASK_APP=login_service.py` in the virtual environment
- In the virtual environment, type `pip install -r requirements.txt` to install the required libraries
- In the virtual environment, type `flask run --port=5000` to start the microservice
### 
- In the _assignment2/_ directory, open a new terminal and type `. venv/bin/activate` to start the virtual environment
- Type `export FLASK_APP=url_shortener_service.py` in the virtual environment
- In the virtual environment, type `pip install -r requirements.txt` to install the required libraries
- In the virtual environment, type `flask run --port=5001` to start the microservice

## 2. Using the microservices:
- Start the Postman application
- Direct the REST calls for the login service to http://localhost:5000/
    - To create/login a user, pass the _username_ and _password_ as parameter keys in Postman, with appropriate values
    - Once a user has been created using the login service (and then logs in), a JWT access token will be generated and returned
    - This key can now be used with the url shortener service
- Direct the REST calls for the url shortener service to http://localhost:5001/
    - Most REST calls in this service require use of the JWT access token generated by the login service
    - In Postman, add this token as a _Bearer Token_ type, under the _Authorization_ tab
    - All REST calls should now be permitted
    - To add a new web address to shorten (via POST), add the _url_ as a parameter key, and the address as the value