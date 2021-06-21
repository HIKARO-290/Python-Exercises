mulheres = 0
homens = 0
maiorDeIdade = 0
sair = False
while not sair:
    pessoaIdade = int(input("digite a idade desta pesssoa"))
    pessoaSexoB = input("digite o sexo biologico desta pessoa").lower().strip()
    if pessoaSexoB.startswith("m"):
        homens += 1
    else:
        if pessoaIdade < 20:
            mulheres += 1
    if pessoaIdade >= 18:
        maiorDeIdade +=1
    if input("deseja sair").lower().strip().startswith("s"):
        sair = True
print(f"existem {homens} homens cadastrados, {mulheres} com menos de 20 anos e, {maiorDeIdade} que possuem mais de 18 anos")