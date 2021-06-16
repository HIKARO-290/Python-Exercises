pares = 0
soma = 0
for i in range(6):
    numero = int(input("digite um valor"))
    if numero % 2 ==0:
        pares +=1
        soma += numero
print(f"A soma entre os valores pares é de {soma} e a quantidade de numeros pares digitados é de {pares}")