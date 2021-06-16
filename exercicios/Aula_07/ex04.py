pares = 0
for i in range(7):
    idade = int(input("digite seu ano de nascimento"))
    idade = 2021 - idade
    if idade < menor or menor == 0:
        menor = idade
    if idade > maior:
        maior = idade
print(f"o pessoa mais velha tem {maior} anos e a mais nova {menor} anos")