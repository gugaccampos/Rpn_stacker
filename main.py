import RPN_stacker as Rpn

while True:
    # Type a expression like the follow: 1 4 + 5 * 6 /
    # If you want to finnish the operations, type 'End'
    operation = input()
    if operation == 'End':
        print('All the operations are done.')
        break
    else:
        result = Rpn.rpn_stacker(operation)
        if type(result) == int:
            print(f'Result = {result}')

        else:
            print(result)
