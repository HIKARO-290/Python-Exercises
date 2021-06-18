perguntas = list(["Telefonou para a vítima? ","Esteve no local do crime? ","Mora perto da vítima? ","Devia para a vítima? ","você ja trabalhou com a vítima? "])
result = 0
resposta = ""
for i in perguntas:
    result = input(i).strip().lower()
    