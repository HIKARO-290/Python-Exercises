valor1 = int(input("1º valor decimal: "))
valor2 = int(input("2º valor decimal: "))
binarios = list()
def converteParaBinario(valor):
    binario = list()
    while valor > 0:
        binario.append(valor%2)
        valor = valor//2
    binario = list(reversed(binario))
    binarios.append(binario)
def comparaBinarios():
    cont = 0
    if len(binarios[0])>len(binarios[1]) or len(binarios[0])>len(binarios[2]):
        cont = len(binarios[0])
    elif len(binarios[1])>len(binarios[2]):
        cont = len(binarios[1])
    else:
        len(binarios[2])
    for i in range(cont - len(binarios[0])):
        binarios[0].insert(0,0)
    for i in range(cont - len(binarios[1])):
        binarios[1].insert(0,0)
    for i in range(cont - len(binarios[2])):
        binarios[2].insert(0,0)

converteParaBinario(valor1)
converteParaBinario(valor2)
converteParaBinario(valor1^valor2)
comparaBinarios()

print(binarios[0])
print(binarios[1])
print(binarios[2]," é o resultado da subtração binária.")
print("onde seu respectivo valor em decimal é:",valor1^valor2)
