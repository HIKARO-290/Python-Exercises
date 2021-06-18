frase = "O joão Foi andar ,de bicicleta."
frase_02 = 'A maria não gosta de bicicleta'
#seleção por posição (index)
print(frase[5])
#seleção por intervalo (index e quantidade de casas)
print(frase[2:6])
#seleção por intervalo (index , quantidade e passo)
print(frase[5:1:-1])
#substituição por low case (letra minúscula )
print(frase.lower())
#substituição por upper case (letra maiúscula)
print(frase.upper())
# função title substitui a primeira letra de toda palavra na istring por upper case(letra maiúscula)
print(frase.title())
# função captalize torna todas as letra da frase minúsculas além de tornar a primeira letra da frase em maiúsculo
print(frase.capitalize())
# swapcase inverte letras maiúsculas se tornam minúsculas vice e versa
print(frase.swapcase())
#ljust ajusta o valor da string para o tamanho definido
frase = frase.ljust(50)
frase += "!" #concatenação de strings (mesmo que frase = frase + "!")
print(frase)
#split separa todos os itens dentro de uma string em uma lista
print(frase.split())
#replace substituir um iten por outro dentro da string
print(frase.replace(",","."))
#strip remove todos caracteres definidos no inicio da string
print(frase.strip("O, "))
#center ajustar a string adicionando espaços necessários no inicio e no fim da string
print(frase.center(100))
#find procura e retorna a posição de um valor
print(frase.find("a"))
#startswith retorna true ou false em caso a string começar com um valor determinado
print(frase)
print(frase.startswith('O'))
#endswith retorna // // em caso de a string finalizar com um valor determinado
print(frase.endswith('!'))
#islower retorna true ou false em caso de a frase possuir apenas letras minusculas ou não
print(frase.lower().islower())
#isupper //                                                      letras maiúsculas ou não
print(frase.upper().isupper())
#type retorna tipo de variavel
print(type(frase))
print(type(1))
#count retorna quantidade de itens
print(frase.count('o'))
#len() retorna tamanho string
print(len(frase))

