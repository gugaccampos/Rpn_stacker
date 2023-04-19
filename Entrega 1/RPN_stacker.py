def operation_procedures(stack, operator):

    num1 = stack.pop(0)
    num2 = stack.pop(0)
    if operator == "+":
        stack.append(num1 + num2)
        return 1

    elif operator == "-":
        stack.append(num1 - num2)
        return 1

    elif operator == "/":
        stack.append(num1 / num2)
        return 1

    elif operator == "*":
        stack.append(num1 * num2)
        return 1

    else:
        return 0


def rpn_stacker(operation):
    stack = []
    x = 1
    elements = operation.split()
    for element in elements:
        if x == 0:
            break
        if element.isdigit():
            stack.append(int(element))
        else:
            x = operation_procedures(stack, element)

    if x == 1:
        return stack.pop()

    else:
        return 'The requested operation is not supported by this calculator'
