#faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
# e ‘N’, se seu argumento for zero ou negativo.
def verify(response):
    if response.lower() == "positivo":
        return 'P'
    elif response.lower() == "negativo" or response == "0":
        return 'N'
    else:
        return 'valor invalido'
send = input("digite se gosta ou não de abacaxi: com positivo ou negativo: ")
print(f"A sua resposta foi: {verify(send)}")