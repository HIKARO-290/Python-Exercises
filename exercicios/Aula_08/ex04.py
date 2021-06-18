perguntas = list(["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","você ja trabalhou com a vítima? "])
resposta = ""
resultado =list(["Inocente","Suspeita","Cumplice","Cumplice","Assassino"])
culpa = 0
for i in range(5):
    resposta = input(perguntas[i]).strip().lower()
    if resposta.startswith("s"):
        culpa += 1
if culpa == 1:
    print(f"Você é um(a): {resultado[culpa]}")
else:
    print(f"Você é um(a): {resultado[culpa-1]}")


