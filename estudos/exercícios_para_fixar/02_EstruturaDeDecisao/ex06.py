# Faça um Programa que leia três números e mostre o maior deles.
firstnumber = float(input("Enter with the first number: "))
secondnumber = float(input("Enter with the second number: "))
thirdnumber = float(input("Enter with the third number: "))

if firstnumber > secondnumber and firstnumber > thirdnumber:
    print(firstnumber)
elif secondnumber>thirdnumber:
    print(secondnumber)
else:
    print(thirdnumber)