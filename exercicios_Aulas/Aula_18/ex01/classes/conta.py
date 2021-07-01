class Conta:
    def __init__(self,titular="",saldo=0):
        self.titularconta = titular
        self.saldoconta = saldo
    def __str__(self):
        return print("imprimir isto kkk")

    def sacarEmConta(self,valor):
        if valor == 0:
            return print("valor invalido!")
        elif self.saldoconta > valor:
            self.saldoconta -=valor
            return print("saque realizado com sucesso!")
        else:
            return print("Você não possui saldo suficiente!")
    def depositarEmConta(self,valor):
        self.saldoconta+=valor
        return print(f"Seu novo saldo é de:{self.saldoconta:.2f}")
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
