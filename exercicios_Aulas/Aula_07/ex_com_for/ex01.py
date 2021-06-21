

maior = 0.0
menor = 0.0

for i in range(5):
    pessoa = float(input("digite o peso da primeira pessoa"))
    if pessoa < menor or menor == 0.0:
        menor = pessoa
    if pessoa > maior:
        maior = pessoa
print(f"o maior valor e {maior:.2f} o menor peso é {menor:.2f}")