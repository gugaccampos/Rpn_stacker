import re

def isNum(symbol: str):
    token = re.findall("[0-9]", symbol)
    if token:
        return True
    return False

def isOP(symbol: str):
    token = re.findall("[+-/*]", symbol)
    if token:
        return True
    return False


def operation_procedures(stack, operator):

    num1 = stack.pop(0)
    num2 = stack.pop(0)
    if operator[0] == "TYPE = PLUS":
        x = (num1 + num2)
        return x

    elif operator[0] == "TYPE = MINUS":
        x = (num1 - num2)
        return x

    elif operator[0] == "TYPE = SLASH":
        x = (num1 / num2)
        return x

    elif operator[0] == "TYPE = STAR":
        x = (num1 * num2)
        return x

def classify_tokens(token):
    classifyer = []

    if isNum(token):
        classifyer.append('TYPE = NUM')
        classifyer.append(f'lexeme = {token}')
    elif isOP(token):
        if token == '*':
            classifyer.append('TYPE = STAR')
            classifyer.append(f'lexeme = {token}')
        elif token == '-':
            classifyer.append('TYPE = MINUS')
            classifyer.append(f'lexeme = {token}')
        elif token == '+':
            classifyer.append('TYPE = PLUS')
            classifyer.append(f'lexeme = {token}')
        elif token == '/':
            classifyer.append('TYPE = SLASH')
            classifyer.append(f'lexeme = {token}')

    return classifyer

def rpn_stacker(operation):
    stack = []

    for element in operation:

        if element[0] == 'TYPE = NUM':
            stack.append(int(element[1][8:]))
        else:
            result = operation_procedures(stack, element)
            stack.append(result)

    return stack.pop()




with open('Calc.stk', 'r') as inputs:
    calculator = inputs.readlines()

tokens = []
checker = False

for line in calculator:
    line = line.replace('\n', '')
    line.rstrip()

    if line == '':
        continue

    if isNum(line) or isOP(line):

        token = classify_tokens(line)
        tokens.append(token)

    else:
        print('The requested operation is not supported by this calculator')
        checker = True
        break


if not checker:
    result = rpn_stacker(tokens)
    print(f'Result = {result}')