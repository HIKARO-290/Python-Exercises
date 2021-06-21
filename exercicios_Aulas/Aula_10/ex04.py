cadastro = list()
contador = 1
while True:
    cadastro.append([input("digite seu nome: "),float(input("digite eu peso"))])
    if input("deseja continuar?").lower().strip(" ").startswith("n"):
        break
    contador += 1
print(f"A quantidade de pessoas cadastradas é: {contador} \nO maior peso é de {max(cadastro)}\nO menor peso é de: {min(cadastro)}")