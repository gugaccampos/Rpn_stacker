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

    if token.isdigit():
        classifyer.append('TYPE = NUM')
        classifyer.append(f'lexeme = {token}')
    else:
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
        else:
            print('The requested operation is not supported by this calculator')
            return 0

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




with open('C:/Users/gugac/Rpn_stacker/Entrega 2/Calc.stk', 'r') as inputs:
    calculator = inputs.readlines()

tokens = []
checker = False

for line in calculator:
    line = line.replace('\n', '')
    line.rstrip()

    token = classify_tokens(line)

    if token == 0:
        checker = True
        break

    tokens.append(token)

result = rpn_stacker(tokens)
print(f'Result = {result}')