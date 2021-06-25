#7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
#forem iguais, imprima que eles são iguais.

#verify and compare the numbers
def verify(number01,number02):
    if number01 == number02:
        return "this two numbers are equals!"
    elif number01 > number02:
        return f"the low number is: {number02}"
    else:
        return f"the low number is: {number01}"
#get values 
def main():
    number01 = float(input("Enter with the first number: "))
    number02 = float(input("Enter with the second number:"))
    return verify(number01,number02)
#show the low number
print(main())