lista = list([list([None,None,None]),list([None,None,None]),list([None,None,None])])
for i in range(3):
    for g in range(3):
        lista[i][g] = int(input(f"digite o valor de [{i}] [{g}]"))
for i in range(3):
    print(lista[i])