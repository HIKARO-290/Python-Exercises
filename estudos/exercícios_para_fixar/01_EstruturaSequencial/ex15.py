#get your salary and the number of hours you worked
#pega o valor do seu salário e a quantas horas você trabalhou
salarybyhour = float(input("Enter with your salary value: "))
hours = float(input("Enter with the number of the hours you worked"))
#perform the salary without discounts
#calcula salario sem descontos
salarybase = salarybyhour*hours
#perform the calculus to put the imposts discounts
#realiza o calculo para adicionar os descontos de impostos
rentip = salarybase * 0.11
print(salarybase)
inss = salarybase * 0.08
sindicateip = salarybase * 0.05
#Show the results
#Mostra os resultados
print(f"""
    + Salary Basy : R$ {salarybase}
    - IR (11%) : R$ {rentip}
    - INSS (8%) : R$ {inss}
    - Sindicato ( 5%) : R$ {sindicateip}
    = Salário Liquido : R$ {salarybase - rentip - inss - sindicateip}
""")