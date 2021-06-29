import sys
from .imports.conta import Conta
contas = dict()
while True:
    if input("você deseja cadastrar uma nova conta?").lower().startswith('n'):
        break
    else:
        titular = input("digite o nome do titular: ")
        contas[titular] = Conta(titular,float(input("digite o Valor inicial desta conta: ")))
 
    operacao = int(input("que operação deseja realizar?\n01-depositar\n02-sacar\n03-cadastrar\n04-Sair "))
    if operacao == 1:
        print("digite o nome do títular da conta que deseja realizar a operação: ")
        for contatitular in contas.keys():
            print("conta de :",contatitular)
        titular = input()
        contas[titular].depositarEmConta(float(input("digite o valor que deseja depositar: ")))
    elif operacao == 2:
        print("digite o nome do títular da conta que deseja realizar a operação: ")
        for contatitular in contas.keys():
            print("conta de :",contatitular)
        titular = input(": ")
        contas[titular].sacarEmConta(float(input("digite o valor que deseja sacar: ")))
    elif operacao == 3:
        titular = input("digite o nome do titular: ")
        contas[titular] = Conta(titular,float(input("digite o Valor inicial desta conta: ")))
    else:
        break