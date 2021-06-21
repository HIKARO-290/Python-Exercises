cadastro = list()
contador = list([0,0])
for cont in range(5):
    client = str(input("digite seu nome: "))+","+ str(input("digite sua idade"))
    cadastro.append(client.split(","))
    if int(cadastro[cont][1]) < 18:
        cadastro[cont].append("menor de idade")
        contador[0] += 1
    else:
        cadastro[cont].append("maior de idade")
        contador[1] += 1
for cont in cadastro:
    print(cont)
print(f"menor de idade tem {contador[0]} \nmaior de idade tem {contador[1]}")