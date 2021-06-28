# Faça um Programa que leia três números e mostre o maior e o menor deles.
firstnumber = float(input("Enter with the first number: "))
secondnumber = float(input("Enter with the second number: "))
thirdnumber = float(input("Enter with the third number: "))

if firstnumber > secondnumber and firstnumber > thirdnumber:
    if secondnumber > thirdnumber:
        print("the lower number is:",thirdnumber)
    else:
        print("the lower number is:",secondnumber)
    print("the high number is:",firstnumber)
elif secondnumber>thirdnumber:
    print("the lower number is:",firstnumber)
    print("the high number is:",secondnumber)
else:
    print("the lower number is:",firstnumber)
    print("the high number is:",thirdnumber)

