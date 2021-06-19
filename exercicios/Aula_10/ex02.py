matriz = list()
for i in range(3):
    temp = list()
    for g in range(3):
        temp.append(int(input(f"digite o valor de [{i}] [{g}]")))
    matriz.append(temp)

for i in range(3):
    print(f"            [   {matriz[i][0]}  ][   {matriz[i][1]}   ][   {matriz[i][2]}   ]")
    