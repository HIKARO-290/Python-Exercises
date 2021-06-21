valor = int(input("digite um valor para gerar a tabuada"))
dividido = 0
print("    multiplicação   | divisão   |   soma    |   subtração")
for i in range(11):
    if i !=0:
        dividido = valor/i
    print(f"    {valor} * {i} = {(valor*i)}    |   {valor} / {i} = {dividido:.1f}  |   {valor} + {i} = {(valor+i)} |   {valor} - {i} = {(valor-i)}")