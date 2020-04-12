# Assignment 1.1: Web Service (WDSL/SOAP)
### The assignment report/answers are in the file: _report_answers.doc_

The following has been tested using RHEL 8.1, Python 2.7, and Java 8 

# Bottom-Up

## This uses the _soaplib_ and _zeep_ libraries for Python 2.7. These can be installed using pip2:
- pip2 install --user soaplib==2.0.0-beta2
- pip2 install --user zeep

## To run the calculator, first start _web_server.py_, followed by _client.py_:
- python2 WebServer/web_server.py
- python2 BottomUpClient/bottom_up_client.py

    (The web service uses localhost port 8000)

## Usage:
- This is a simple calculator, which performs an operation on two real numbers
- Valid operators are: + - * /
- Numbers and operators must be space separated
- Example (valid) user input:
    - 33 / 0.23
    - &nbsp;&nbsp;&nbsp; 2 &nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp; 2
    - 4 * -1337
    - -3.14 - -9
- To exit the program from terminal, press ctrl+z

# Top-Down

## Requirements (recommended):
- Java 8 (or higher) and Eclipse or Netbeans IDE
- The requirements from "Bottom-Up"

## Usage:
- Start the Python web server
    - python2 WebServer/web_server.py
- Import the project _TopDownClient_ into one of the above IDE's
- Navigate to the _Client.java_ file in the _src/tns/_ directory
- From the IDE, click/select "Run"
- Output will be displayed in the terminal for four pre-defined calls to _web_server.py_