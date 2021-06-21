import random
jogos = int(input("quantos jogos desejam fazer"))
lista = list()
for i in range(jogos):
    lista.append(random.sample(range(1,61),6))
print(lista)