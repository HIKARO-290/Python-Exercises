# Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

listpersons = list()
middle = 0
result =""
ageslist = ""
while True:
    person = dict()
    person['name'] = input("digite seu nome: ")
    person['biologicsex'] = input("digite qual seu sexo biológico: masculino ou feminino: ").lower().strip(" ")
    person['age'] = int(input("digite sua idade: "))
    listpersons.append(person)
    if input("gostaria de adicionar mais um cadastro? ").lower().startswith("n"):
        break
#inicia verificações
for i in listpersons:
    if i['biologicsex'].lower().strip(" ").startswith("f"):
        result +=f"{i['name']},"
#soma as idades
    middle += i['age']
#determina a média das idades
middle = int(middle/len(listpersons))
#vefica idades acima da média
for i in listpersons:
    if i['age'] > middle:
        ageslist += str(i['age'])+","
#exibe quantidade de cadastros     
print(f"""No cadastro existem: {len(listpersons)} pessoas, 
onde a média de idade é de: {middle} 
e constam como mulheres apenas: {result} 
as idades acima da média são: {ageslist}""")


