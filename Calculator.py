def number_entry():
    '''
    This function deals with number entry and pushes numbers entered into a list
    '''
    nlist = []


    while True: #loop to prevent ghost entries

        number = (input('enter number:'))

        try:
            number = int(number)
            nlist.append(number)
            break
        except:
            print("error, please enter numeric values only")
            

    while True:

        n_entry = input('do you wanna enter any more numbers? yes/no?')
        if n_entry == 'yes':
            try:
                numbers = int(input('enter number:'))
                nlist.append(numbers)
            except:
                print('enter valid number')
        elif n_entry == 'no':
            break
        else:
            print("please enter yes or no only.")
    return nlist
            

def operator_entry():
    '''
    This function deals with operator entry, pushing operators in string form into a list
    '''
    first_op = input('enter operator:')
    op_list = []


    while True: #loop to prevent ghost entries

        if first_op  in ['+', '-', '*','/']:
            op_list.append(first_op)
            break
        else:
            first_op = input('please enter a valid operator:')
        

    while True:

        nops = input('do you wanna enter another operation? yes or no?:')
        if nops == 'yes':
            op = input('enter operator:')
            if op in ['+', '-', '*','/']:
                op_list.append(op)
            else:
                print("please enter valid operator.")
                break
        elif nops == 'no':
            break
        else:
            print("enter yes/no only.")
            
    return op_list
    

def calculation(nlist, op_list):
    '''
    This function calculates the result of the numbers and operators
    '''
    result = nlist[0]

    lo = len(op_list)
    ln = len(nlist)

    if ln < 2:
        print("youve entered only one number, hence no operation applies")
    elif lo != ln-1:
        print('enter 1 less no. of operators than numbers. eg: numbers = 10, operators = 9')
    else:
        for i in range (0, lo):
            
            if op_list[i] == '+':
                result = result + nlist[i+1]
            elif op_list[i] == '-':
                result = result - nlist[i+1]
            elif op_list[i] == '/':
                if nlist[i+1] == 0:
                    print('division by zero is not feasible')
                    return
                elif nlist[i] == 0 and nlist[i+1] != 0:
                    print('dividing by zero is not feasible')
                    return
                else:
                    result = result / nlist[i+1]
            elif op_list[i] == '*':
                result = result * nlist[i+1]
            
        print(f'the numbers are: {nlist}')
        print(f'the operators are {op_list}')
        print(f'the result is: {result}')    


def calculator():
    '''
    This function calls all functions
    '''
    nlist = number_entry()
    op_list = operator_entry()
    calculation(nlist,op_list)

if __name__ == "__main__": #only runs the file when executed directly. so no import issues.
    calculator()
