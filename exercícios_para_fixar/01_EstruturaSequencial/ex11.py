#get the two integers numbers
#pega os dois números inteiros
numero1 = int(input("digite o primeiro número inteiro: "))
numero2 = int(input("digite o segundo número inteiro: "))
#get the real number
#pega o numero real
numero3 = float(input("digite o terceiro número, porem deve ser um numero real: "))
#perform the calculus
#realiza os calculos
produto = numero1*(numero2/2)
soma = (3*numero1)+numero3
pontencia = numero3**3
#Show the results
#mostra os resultados
print(f"""
O produto entre a metade do segundo com o primeiro número é: {produto}
A soma do triplo do primeiro numero com o terceiro numero é: {soma}
O valor do terceiro número elevado ao cubo é : {pontencia}
""")