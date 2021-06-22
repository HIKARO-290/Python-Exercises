#get the fish weight
#pega o peso de peixes
weight = float(input("Enter with the the fish weight: "))
#verify if the weight is more or less than 50
# verifica se o peso é mais ou menos que 50
if  weight > 50:
#perform the calculus for the penalty and show the value
#realiza o calculo da penalidade e mostra o valor
    penalty = (weight-50)*4.00
    print(f"The penalty for this time is: $ {penalty}")
else:
#Show to the fisherman he don't have penalty
#mostra para o pescador que o mesmo não possui penalidade
    print("The fisherman don't have to pay anything this time.")