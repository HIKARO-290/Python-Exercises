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
