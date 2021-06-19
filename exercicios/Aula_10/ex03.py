matriz = list()
soma = 0
resultado = ""
for i in range(3):
    temp = list()
    for g in range(3):
        temp.append(int(input(f"digite o valor de [{i}] [{g}]")))
    matriz.append(temp)
#realiza a soma dos valores pares
for i in range(3):
    for g in range(3):
        if matriz[i][g]%2==0:
            soma = soma+matriz[i][g]
resultado += "A soma de todos os valores é: "+str(soma)
#soma os valores da terceira coluna e apresenta a matriz
soma = 0
for i in range(2,-1,-1):
    soma = soma + matriz[i][2]
    print("esta é a matriz")
    resultado = f"            [   {matriz[i][0]}  ][   {matriz[i][1]}   ][   {matriz[i][2]}   ]\n" + resultado
#mostra o resultado
resultado+="\nA soma dos valores da terceira coluna é: "+str(soma)+"\nO maior valor da segunda linha é: "+ str(max(matriz[1]))
print(resultado)