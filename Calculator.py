num1 = input("Enter first number:")
num2 = input("Enter second number:")
operation = input("Enter operator ( +, - , / , * ) :")

num1 = int(num1)
num2 = int(num2)

if operation == "+":
    soln = num1 + num2
    print(f'the solution is : {soln}')

elif operation == "-":
    soln = num1 - num2
    print(f'the solution is : {soln}')

elif operation == "/":
    soln = num1 / num2
    print(f'the solution is : {soln}')

elif operation == "*":
    soln = num1 * num2
    print(f'the solution is : {soln}')
