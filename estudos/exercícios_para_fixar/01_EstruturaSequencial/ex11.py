#get the two integers numbers
#pega os dois números inteiros
number1 = int(input("Enter with the first number: "))
number2 = int(input("Enter with the second number: "))
#get the real number
#pega o numero real
number3 = float(input("Enter with the third number, but this number has to be a real number: "))
#perform the calculus
#realiza os calculos
product = (2*number1)*(number2/2)
sumofnumbers = (3*number1)+number3
potential = number3**3
#Show the results
#mostra os resultados
print(f"""
The product from half of the second number with the double of the first number is: {product}
The sum from the triple of the first number with the third number is: {sumofnumbers}
The value of the third number to the 3 power : {potential}
""")