#get the value of a client height
#pega o valor da altura do cliente
height= float(input("Enter with your height "))
#get the sex type of the client
#pega o sexo do cliente
sex = input("what is your sex type: ").lower()
#verify if the client is a man and if the client is a man perform one calculus
#verifica se o cliente é homem e se for homen realiza um calculo
if sex.startswith("m"):
    weight = (72.7*height)-58
    print("this person with man sex need have to weight in max like: ",weight)
#if the client is not a man perform the other colculus
#Se o cliente nao for homen realiza outro calculo
else:
    weight = (62.1*height)-44.7
    print("this person with womam sex need have to weight in max like: ",weight)