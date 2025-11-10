num1 = input("Enter first number:")
num2 = input("Enter second number:")

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

try:
    num1 = int(num1)
    num2 = int(num2)
    valid_input = True
except:
    print("error, please enter numeric values")
    valid_input = False

if valid_input == True:
    calc(num1,num2)
else:
    print("could not call function due to valueerror")

