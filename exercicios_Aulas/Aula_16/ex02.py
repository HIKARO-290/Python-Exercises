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

contapessoal01 = Conta("juão",0)
contapessoal01.depositarEmConta(1300)
contapessoal01.sacarEmConta(200)
contapessoal01.sacarEmConta(1200)
