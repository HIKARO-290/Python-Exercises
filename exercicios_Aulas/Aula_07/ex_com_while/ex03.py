produtoNome = ""
produtoValor = ""
acimaDeMil = 0
baratoPreco = 0.0
baratoNome = ""
sair = False
valorTotal = 0.0
while not sair:
    produtoNome = input("digite o nome do produto")
    produtoValor = float(input("digite o valor do produto"))
    valorTotal += produtoValor
    if produtoValor > 1000:
        acimaDeMil += 1
    if produtoValor < baratoPreco or baratoPreco==0.0:
        baratoNome = produtoNome
    if input("Deseja sair? \n").lower().strip().startswith("s"):
        sair = True
print(f"""O total da compra é de {valorTotal},
A quantidade de produtos com valor acima de 1000.00 é de: {acimaDeMil}
O produto mais barato foi: {baratoNome}
""")