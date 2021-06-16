import random
#######################
# exercicio 01
print("exercício 01")
#######################
senha = input("digite a senha")
while senha != "babalu":
    senha = input("senha incorreta digite novamente:")
print("senha correta")
#######################
# exercicio 02
print("exercício 02")
#######################
teste = 0
resposta = input("digite M | F para declarar seu sexo biológico").upper().strip()
while teste != 1:
    if resposta.startswith("M") or resposta.startswith("F"):
        teste = 1
    else:
         resposta = input("valor digitado incorreto. Digite novamente").upper().strip()
#######################
# exercicio 03
print("exercício 03")
#######################

clarividencia = random(11)
tentativa = int(input("Eu sou seu computador e mostrarei meus poderes mediunicos para pensar no ultimo numero que vc escolheria \n, digite um numero e eu direi se está correto: \n"))
cont=0
while clarividencia != tentativa:
    cont+=1
    if clarividencia < tentativa:
        tentativa = int(input("Você errou o número é menor do que este"))
    elif clarividencia > tentativa:
        tentativa = int(input("Você errou o número é maior do que este"))
print("parabens parece que meus poderes mediúnicos não são tão bons assim, porem você precisou de {cont}tentativas para acert")