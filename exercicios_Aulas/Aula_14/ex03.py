#function to perform one sum from impost and the current value
def somaImposto(taxaimposto=0,custo=0):
    return (custo - altera(taxaimposto,custo))
#function to perform one convertion from one percent number to perform de calculus
def altera(taxaimposto=0,custo=0):
    return (taxaimposto*custo/100)
#function to have one interaction with the client
def pegavalores():
    arg01 = float(input("digite o valor da taxa de impostos em %"))
    arg02 = float(input("digite o valor a deduzir os impostos"))
    return somaImposto(arg01,arg02)
#show the final result from the all process
print("o valor restante após cobrança do imposto é de:",pegavalores()) 