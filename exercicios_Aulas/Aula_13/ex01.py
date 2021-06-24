# Faça um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de
#  uma pessoa, retornando um valor literal indicando se
#  uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(nascimento):
    tempo = 2021 - nascimento
    if tempo < 16:
        return "Negado"
    elif 16>=tempo or tempo<18 or tempo>=70:
        return "Opcional"
    else:
        return "Obrigatório"

ano = int(input("digite seu ano de nascimento: "))
print(f"Tendo Nascido em {ano} Seu voto é ",voto(ano))