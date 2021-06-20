from random import randint
lista = list(["dois","um"])
maquina = randint(0,10)

for i in range(5):

    pergunta = list([input("par ou impar? \n"),int(input("valor de 1 a 10: "))])
    print(f"a maquina decidiu jogar: {maquina}")

    if (pergunta[1] + maquina)%2 == 0:
        if pergunta[0] == "par":
            print("você ganhou")
        else:
            print("você perdeu")
    else:
        if pergunta[0] == "impar":
            print("você ganhou")
        else:
            print("você perdeu")

    
