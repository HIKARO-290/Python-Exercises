class Conta:
    def __init__(self,titular="",saldo=0):
        self._titularconta = titular
        self._saldoconta = saldo
    def __str__(self):
        return print("imprimir isto kkk")
    def _pode_sacar(self,valor):
        return self._saldoconta > valor
    def sacarEmConta(self,valor):
        if valor == 0:
            return print("valor invalido!")
        elif self._pode_sacar(valor):
            self._saldoconta -=valor
            return print("saque realizado com sucesso!")
        else:
            return print("Você não possui saldo suficiente!")
    def depositarEmConta(self,valor):
        self._saldoconta+=valor
        return print(f"Seu novo saldo é de:{self._saldoconta:.2f}")
    def validanome(self):
        if self._titularconta.isnumeric():
            return 0
        else:
            return 1
    def validavalor(self,valor):
        if valor.isnumeric():
            return float(valor)
        else:
            return 0
    @property
    def saldo(self):
        return self._saldoconta
    @property
    def titular(self):
        return self._titularconta
    @saldo.setter
    def saldo(self,saldo):
        self._saldoconta = saldo
    @titular.setter
    def titular(self,titular):
        self._titularconta = titular
    