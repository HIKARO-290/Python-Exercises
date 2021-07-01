from classes.conta import Conta
if __name__ == '__main__':
    contas = dict()
    while True:
        operacao = int(input("que operação deseja realizar?\n01-depositar\n02-sacar\n03-cadastrar\n04-Sair \n"))
        if operacao == 1:
            valor=True
            while valor:
                print("digite o nome do títular da conta que deseja realizar a operação: ")
                for contatitular in contas.keys():
                    print("conta de :",contatitular)
                titular = input()
                if titular.isnumeric():
                    print("Valor incorreto digite novamente")
                else:
                    contas[titular].depositarEmConta(float(input("digite o valor que deseja depositar: ")))
                    valor = False
        
        elif operacao == 2:
            print("digite o nome do títular da conta que deseja realizar a operação: ")
            for contatitular in contas.keys():
                print("conta de :",contatitular)
            titular = input("\n: ")
            if titular.isnumeric():
                print("Valor incorreto digite novamente")
            else:
                contas[titular].sacarEmConta(float(input("digite o valor que deseja sacar: ")))
                continue
        elif operacao == 3:
            titular = input("digite o nome do titular: ")
            if titular.isnumeric():
                print("Valor incorreto digite novamente")
            else:
                contas[titular] = Conta(titular,float(input("digite o Valor inicial desta conta: ")))
                continue
        
        else:
            break