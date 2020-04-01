import zeep

wsdl = 'http://localhost:8000/?wsdl'
client = zeep.Client(wsdl=wsdl)
operators = ['+', '-', '*', '/']

def calculate(val1, op, val2):
    answer = 0

    if op in operators:
        if op == '+':
            answer = client.service.add(val1, val2)
        elif op == '-':
            answer = client.service.sub(val1, val2)
        elif op == '*':
            answer = client.service.mul(val1, val2)
        elif op == '/':
            if val2 == 0:
                print('Error: division by zero')
                return
            answer = client.service.div(val1, val2)
    else:
        print('Error: equation accepts only the following operators +-*/')
        return

    print('{} {} {} = {}').format( val1, op, val2, answer)

if __name__ == "__main__":
    while True:
        try:
            equation = raw_input("\nEnter a simple equation\n").split()

            if len(equation) != 3:
                print('Error: too few/many arguments')
                continue

            value1 = float(equation[0])
            operator = equation[1]
            value2 = float(equation[2])

            calculate(value1, operator, value2)
        except:
            print('Error: equation only accepts real numbers')
