cadastro = list()
for cont in range(5):
    client = str(input("digite seu nome: "))+","+ str(input("digite sua idade"))
    cadastro.append(client.split(","))
    if int(cadastro[cont][1]) < 18:
        cadastro[cont].append("menor de idade")
    else:
        cadastro[cont].append("maior de idade")
for cont in cadastro:
        print(cont)