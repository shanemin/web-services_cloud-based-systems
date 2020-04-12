# Assignment 1.2: RESTful Service
### The assignment report/answers are in the file: _report_answers.doc_

The following has been tested using RHEL 8.1 and Python 3.6

## This uses the _Flask_ library for Python 3.6. Installation instructions can be found here:
- https://flask.palletsprojects.com/en/1.1.x/installation/

## To run the URL shortener, first start _web_server.py_:
- Type `export FLASK_APP=web_server.py` into your terminal, or add it to your ~/.bashrc file
- In the _assignment1/1_2_ directory, type `. venv/bin/activate` in your terminal to start the virtual environment
- In the same directory, type `flask run` in your terminal to start the REST service

    (The web service uses localhost port 5000)

## Usage:
- This is a RESTful URL-shortener service
- REST methods can be tested using a program such as the Postman API Client (https://www.postman.com/)
- Set the address to: http://localhost:5000/
- Perform the various REST operations as described in the assignment description
- To exit the program from terminal, press ctrl+c
