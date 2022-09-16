def power(Number,power) :
    result = 1 
    for i in range(power) :
        result *=Number
    return result
n = input("Please enter the base number :")
p = input("Please enter the power number :")
print("The answer = " + str(power(int(n),int(p))))