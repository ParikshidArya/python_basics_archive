def number_entry():

    global nlist
    nlist = []

    
    number = (input('enter number:'))

    try:
        number = int(number)
        nlist.append(number)
    except:
        print("error, please enter numeric values only")
        #exit()


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
            #exit()

def operator_entry():

    first_op = input('enter operator:')
    global op_list
    op_list = []

    if first_op  in ['+', '-', '*','/']:
        op_list.append(first_op)
    else:
        print(f'please enter valid operator:')
        exit()

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
    

def calculation():

    global soln
    global result
    global lo, ln
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
                if nlist[i] != 0 and nlist[i+1] == 0:
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
    number_entry()
    operator_entry()
    calculation()

calculator()



'''
#for i in range 0, 

def calc(x,y):
    operation = input("Enter operator ( +, - , / , * ) :")
    if operation == "+":
        soln = x + y
        print(f'the solution is : {soln}')

    elif operation == "-":
        soln = x - y
        print(f'the solution is : {soln}')

    elif operation == "/":
        soln = x / y
        print(f'the solution is : {soln}')

    elif operation == "*":
        soln = x * y
        print(f'the solution is : {soln}')

    else:
        print("enter valid operation from specified options.")

if valid_input == True:
    calc(num1,num2)
else:
    print("could not call function due to valueerror")

'''