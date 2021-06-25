#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
#get the value from user
value = float(input("Enter with the value: "))
#verify if the number is positive, negative or neutral
if value > 0:
    print("the number is positive")
elif value <0:
    print("the number is negative")
else:
    print("the number is neutral")