# Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, sabendo que a
#  decisão é sempre pelo mais barato.

price_01 = input("Enter with the price for a first product: ")
price_02 = input("Enter with the price for a second product: ")
price_03 = input("Enter with the price for a third product: ")

if price_01.isalpha() and price_02.isalpha() and price_03.isalpha():
    print("Error")
else:
    price_01 = float(price_01)
    price_02 = float(price_02)
    price_03 = float(price_03)
    #here we perform the validation for a low price
    if price_01 < price_02 and price_01 < price_03:
        print("You has to buy the first product")
    elif price_02 < price_03:
        print("You has to buy the second product")    
    else:
        print("You has to buy the third product")