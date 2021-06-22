#Get the value by hour the user receives
#Pega o valor por hora que o usuário recebe
hours = float(input("Enter with the value of your payment by the hours: "))
#Get the value of hours he works in one month
#Pega a quantidade de horas trabalhadas em um mês
month = int(input("Enter with the number of hours worked in this month: "))
#Perform a calculus to see how much he going receives
#realiza o calculo para verificar quanto ele irá receber
income = hours * month
#Show the salary in this month
#mostra o salario deste mês
print(f"In this month your payment is: R${income:.2f}")
