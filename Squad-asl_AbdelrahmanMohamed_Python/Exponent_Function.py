def power(Number,power) :         
    result = 1                    
    for i in range(power) :       
        result *=Number
    return result
n = input("Please enter the base number :")
p = input("Please enter the power number :")
print("The answer = " + str(power(int(n),int(p))))

# Using built-in function  :
# from math import *
# ans = pow(int(n),int(p))
# print( "The answer = " + str(ans))

# Another solution :
# ans = int(n)**int(p)
# print( "The answer = " + str(ans))