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
    def validanome(self):
        if self.titularconta.isnumeric():
            return 0
        else:
            return 1
    def validavalor(valor):
        if valor.isnumeric():
            return float(valor)
        else:
            return 0
