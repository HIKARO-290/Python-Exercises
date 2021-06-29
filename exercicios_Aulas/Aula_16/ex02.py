#Crie uma classe chamada Conta para simular as 
# operações de uma conta corrente. Sua classe deverá
# ter os atributos Titular e Saldo, e os métodos Sacar
#  e Depositar. Crie um objeto da classe Conta e teste os 
# atributos e métodos implementados.​ Adicione uma regra no método Sacar, 
# onde o usuário só poderá sacar se o Saldo for maior que zero, 
# caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente
#  para essa operação." 

class Conta:
    def __init__(self,titular="",saldo=0):
        self.titularconta = titular
        self.saldoconta = saldo

    def sacarEmConta(self,valor):
        if self.saldoconta > valor:
            self.saldoconta -=valor
            print("saque realizado com sucesso!")
        else:
            print("Você não possui saldo suficiente!")
    def depositarEmConta(self,valor):
        self.saldoconta+=valor
        print("Seu novo saldo é de:",self.saldoconta)
contas = dict()
while True:
    if input("você deseja cadastrar uma nova conta?").lower().startswith('n'):
        break
    else:
        titular = input("digite o nome do titular: ")
        contas[titular] = Conta(titular,float(input("digite o Valor inicial desta conta: ")))
 
    operacao = int(input("que operação deseja realizar?\n01-depositar\n02-sacar "))
    if operacao == 1:
        print("digite o nome do títular da conta que deseja realizar a operação: ")
        for conta in contas.keys():
            print(conta)
        titular = input()
        contas[titular].depositarEmConta(float(input("digite o valor que deseja depositar: ")))
    else:
        print("digite o nome do títular da conta que deseja realizar a operação: ")
        for conta in contas.keys():
            print("conta de :"conta)
        titular = input(": ")
        contas[titular].sacarEmConta(float(input("digite o valor que deseja sacar: ")))
            