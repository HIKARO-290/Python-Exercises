import random
parar = False
valorDigitado = 0
numeroGerado = 0
tentativas = 0
numeroGerado = random.randrange(1,11)
while not parar:
    valorDigitado = int(input("digite um valor"))
    tentativas +=1
    if valorDigitado < numeroGerado:
        print("o numero é maior.")
    elif valorDigitado > numeroGerado:
        print("o numero é menor.")
    else:
        parar = True
        print(f"parabens você acertou, e precisou de {tentativas} para conseguir acertar")