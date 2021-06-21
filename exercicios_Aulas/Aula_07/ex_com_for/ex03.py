menor=0
maior=0
for i in range(7):
    idade = int(input("digite seu ano de nascimento"))
    if (2021 - idade) < 18 or menor == 0:
        menor += 1
    if (2021 - idade) >= 18 or maior == 0:
        maior += 1
print(f"existem {maior} maior de idade, e  {menor} menor de idade anos")