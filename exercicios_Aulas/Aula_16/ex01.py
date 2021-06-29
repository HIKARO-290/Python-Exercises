class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nomepessoa = nome
        self.pesopessoa = peso
        self.idadepessoa = idade
    def engordar(self,caloria):
        if self.idadepessoa >30:
            self.pesopessoa += 2*caloria
        else:
            self.pesopessoa += caloria
    def malhar(self,caloria):
        if self.idadepessoa>30:
            self.pesopessoa -= 2*caloria
        else:
            self.pesopessoa -=caloria
    def imprimePessoa(self):
        print("","nome:",self.nomepessoa,"\n","peso:",self.pesopessoa,"\n","idade:",self.idadepessoa)
    
    

pessoa1=Pessoa
pessoa1.imprimePessoa()
nome = input("digite o nome da pessoa")
peso = float(input("digite o peso da pessoa"))
idade = int(input("digite a idade da pessoa"))
pessoa1 = Pessoa(nome,peso,idade)