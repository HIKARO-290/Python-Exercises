#Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
#1,68 e pese 75kg.

#perform the calculus
def performIMC(weight,height):
    return weight / (height**2)
#enter function - get the values from user
def main():
    weight = float(input("Enter with your weight: "))
    height = float(input("Enter with your height: "))
    return performIMC(weight,height)
#show the result
print(f"The IMC from this person is: {main():.2f}")