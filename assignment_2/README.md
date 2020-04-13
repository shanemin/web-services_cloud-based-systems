# Assignment 2: RESTful Microservices Architectures

The following has been tested using RHEL 8.1, Python 3.6, and Postman 7.21.2 for Linux

## This project uses the _Flask_ and _Flask JWT Extended_ libraries for Python 3.6. Postman is used to test the services. More information can be found here:
- https://flask.palletsprojects.com/en/1.1.x
- https://flask-jwt-extended.readthedocs.io/en/stable
- https://www.postman.com/

## 1. Starting the microservices:
### Login service:
- The easy way:
    - In the _assignment2/_ directory, open a new terminal and type `./run_login_service.sh`
- The not-so-easy way:
    - In the _assignment2/_ directory, open a new terminal and type `. venv/bin/activate` to start the virtual environment
    - Type `export FLASK_APP=login_service.py` in the virtual environment
    - In the virtual environment, type `pip3 install -r requirements.txt` to install the required libraries
    - In the virtual environment, type `flask run --port=5000` to start the microservice

### URL shortener service:
- The easy way:
    - In the _assignment2/_ directory, open a new terminal and type `./run_url_service.sh`
- The not-so-easy way:
    - In the _assignment2/_ directory, open a new terminal and type `. venv/bin/activate` to start the virtual environment
    - Type `export FLASK_APP=url_shortener_service.py` in the virtual environment
    - In the virtual environment, type `pip3 install -r requirements.txt` to install the required libraries
    - In the virtual environment, type `flask run --port=5001` to start the microservice

## 2. Using the microservices:
- 