from math import *
Number1 = input("Please enter the first number :")
Op = input("Please enter an operator :")
if Op == "!" :
    result = factorial(int(Number1) )
    print("The factorial of the number = " + str(result))
else :
    Number2 = input("Please enter the second number :")
    if Op == "+" :
        result = float(Number1) + float(Number2)
        print("The sum of the two numbers = " + str(result))
    elif Op == "-":
        result = float(Number1) - float(Number2)
        print("The difference between the two numbers = " + str(result))
    elif Op == "*":
        result = float(Number1) * float(Number2)
        print("The product of the two numbers = " + str(result))
    elif Op == "/":
        result = float(Number1) / float(Number2)
        print("The first number divided by the second number = " + str(result))
    else :
        print("Invalid operator")
