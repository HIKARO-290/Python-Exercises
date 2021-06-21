entrada = tuple()
quantidade = 0
primeiro = 0
for i in range(4):
    valor = int(input("digite um valor"))
    entrada = entrada + tuple([valor])

print(entrada)
quantidade = entrada.count(9)
primeiro = entrada.index(3)
print(f"""o 9 apareceu {quantidade} 
vezes, e o primeiro 3 digitado encontra-se na posição {primeiro}
""")
