#function to sum args created
def sumArgs(arg01=0,arg02=0,arg03=0):
    somar = arg01 + arg02 + arg03
    return somar
def getArgs():
#get all values of args from user
    arg01 = float(input("Enter with the first number "))
    arg02 = float(input("Enter with the second number "))
    arg03 = float(input("Enter with the third number "))
#call the function to perform one sum
    return sumArgs(arg01,arg02,arg03)
#Show the result of the sum
print("The result of this sum is:",getArgs())