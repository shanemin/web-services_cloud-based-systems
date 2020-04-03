# Assignment 1.1: Web Service (WDSL/SOAP)

The following has been tested using RHEL 8.1 and Python 2.7

## This uses the _soaplib_ and _zeep_ libraries for Python 2.7. These can be installed using pip2:
- pip2 install --user soaplib==2.0.0-beta2
- pip2 install --user zeep

## To run the calculator, first start _web_server.py_, followed by _client.py_:
- python2 web_server.py
- python2 client.py

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