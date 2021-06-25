#get the numbers
number1 = float(input("Enter with the first number: "))
number2 = float(input("Enter with the second number: "))
#verify the high number
if number1 > number2:
    print("the high number is:",number1)
elif number2 > number1:
    print("the high number is:",number2)
else:
    print("the two numbers are equals")