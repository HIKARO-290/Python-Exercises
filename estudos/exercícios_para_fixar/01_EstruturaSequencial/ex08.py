#Get the value by hour the user receives
#Pega o valor por hora que o usuário recebe
hora = float(input("digite o valor recebido por hora: "))
#Get the value of hours he works in one month
#Pega a quantidade de horas trabalhadas em um mês
mes = int(input("digite a quantidade de horas trabalhadas no mês: "))
#Perform a calculus to see how much he going receives
#realiza o calculo para verificar quanto ele irá receber
renda = hora * mes
#Show the salary in this month
#mostra o salario deste mês
print(f"Seu salário será de: R${renda:.2f}")
