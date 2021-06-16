maior = 0
menor = 0
for i in range(7):
    idade = int(input("digite seu ano de nascimento"))
    idade = 2021 - idade
    if idade < 18 or menor == 0:
        menor = idade
    if idade >= 18 or maior== 0:
        maior = idade
print(f"existem {maior} maior de idade, e  {menor} menor de idade anos")