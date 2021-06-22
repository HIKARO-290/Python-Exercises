pessoa = dict()
pessoa["nome"] = input("digite seu nome: ")
pessoa["idade"] = (2021 - int(input("digite seu ano de nascimento: ")))
pessoa["ctps"] = int(input("digite seu registro ctps: "))
if pessoa["ctps"]!=0:
    pessoa["anos_de_trabalho"] = int((2021-int(input("digite o ano que fora contratado: "))))
    pessoa["salário"] = float(input("digite o valor de seu salário: "))
    tempo = 35 - pessoa["anos_de_trabalho"]
    print(f"""
   - A pessoa: {pessoa['nome']}, 
   - atualmente com {pessoa['idade']} anos, 
   - identificada pela ctps nº: {pessoa['ctps']}
   - com atual salário de: {pessoa['salário']}
   - precisará de {tempo} anos para poder se aposentar""")
else:
    print(f"""
   - A pessoa {pessoa['nome']} , 
   - atualmente com {pessoa['idade']} anos 
   - não possui carteira de trabalho,
   - e ainda precisa completar 35 anos de trabalho para se aposentar""")

