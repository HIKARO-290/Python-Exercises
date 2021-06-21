voto = 0
candidato01 = 0
candidato02 = 0
candidato03 = 0
candidato04 = 0
nulo = 0
branco = 0
fimVotacao = False
while not fimVotacao:
    print("""
    ----------------------
    |1| José            |
    |2| João            |
    |3| Barney          |
    |4| Alex            |
    |5| voto nulo       |
    |6| voto em branco  |
    \n """)
    voto = int(input("digite sua opção de voto: "))
    if voto == 1:
        candidato01 +=1
    elif voto == 2:
        candidato02 +=1
    elif voto == 3:
        candidato03 +=1
    elif voto == 4:
        candidato04 +=1
    elif voto == 5:
        nulo +=1
    elif voto == 6:
        branco +=1
    else:
        fimVotacao = True
        print("valor digitado invalido!")
print(f"""
    ---------------------------------
    |   opção           |   votos   |
    ---------------------------------
    |1| José            |   {candidato01}       |
    |2| João            |   {candidato02}       |
    |3| Barney          |   {candidato03}       |
    |4| Alex            |   {candidato04}       |
    |5| voto nulo       |   {nulo}       |
    |6| voto em branco  |   {branco}       |
    ---------------------------------
    |A percentagem de votos nulos são: {(nulo*100/(candidato01+candidato02+candidato03+candidato04+branco+nulo)):.2f} %   |
    |A percentagem de votos em branco são: {(branco*100/(candidato01+candidato02+candidato03+candidato04+branco+nulo)):.2f} % |
""")