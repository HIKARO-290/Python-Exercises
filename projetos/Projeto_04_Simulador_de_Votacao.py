# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação
from datetime import datetime
from time import sleep
import os

votos = list()
contadorvotos = list([0,0,0,0,0])

opcoes = """- 1 - Pedrinho da carroça.- 2 - Ordenhador de Sapo.- 3 - Catador de grão de poeira.- 4 - Voto Nulo.- 5 - Voto em Branco"""

def autoriza_voto(anodenascimento):
    date = datetime.now()
    anos = date.year - anodenascimento
    if anos > 16 and anos < 18 and anos > 70:
        return 'OPCIONAL'
    elif anos < 16:
        return 'NEGADO'
    else:
        return 'OBRIGATÓRIO'
def votacao(autorizacao,valorvoto):
    voto = dict()
    if autorizacao == 'NEGADO':
        return 'Você não pode votar!'
    else:
        contadorvotos[valorvoto-1]+=1
        votos.append(voto)
        return 'Voto realizado com sucesso!'
def mostra_candidatos():
    tabela = " ".center(52).replace(" ","_")+"\n"
    tabela+= "|"+"candidatos e opções".center(50)+"|\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|\n"
    opcao = opcoes.split(".")
    for i in range(5):
       tabela+=f"|{opcao[i].ljust(50)}|\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|\n"
    return tabela
def imprime_resultado():
    tabela = " ".center(58).replace(" ","_")+"\n"
    tabela += "|"+"candidatos e opções".center(50)+"|votos|\n"
    tabela += "| ".ljust(51).replace(" ","_")+"|_____|\n"
    opcao = opcoes.split(".")
    for i in range(5):
       tabela+=f"|{opcao[i].ljust(50)}|{str(contadorvotos[i]).center(5)}|"+"\n"
    tabela+="|"+" ".center(50).replace(" ","_")+"|_____|\n"
    tabela+=f"\n O vencedor nesta votação é:{opcao[(contadorvotos.index(max(contadorvotos)))]}"
    return tabela
def espera(numeroespera):
    os.system('cls' if os.name == 'nt' else 'clear')
    esperar = ""
    for i in range(numeroespera):    
        esperar += "● "
        print(esperar)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
existeoutroeleitor="s"
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if existeoutroeleitor.startswith("s"):
        nascimentoeleitor = int(input("digite o ano de nascimento do eleitor: "))
        autoriza = autoriza_voto(nascimentoeleitor)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Seu status para votação é de:",autoriza)
        sleep(2)
        espera(3)
        print(mostra_candidatos())
        valorvoto = int(input("digite sua escolha: "))
        espera(3)
        print(votacao(autoriza,valorvoto))
        sleep(3)
        espera(3)
        existeoutroeleitor = input("Existe um próximo eleitor? ").strip(" ").lower()
        
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Contabilizando votos .")
        sleep(1)
        espera(10)
        print(imprime_resultado())
        break

