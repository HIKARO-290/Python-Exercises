#03 - Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de
# AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo
# que nesses casos Fevereiro terá 29 dias.
#import libre to format the date
from datetime import datetime
#perform the conversion
def convertDate(year,month,day):
    date = datetime(year,month,day)
    months=("Janeiro","fevereiro","maço","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
    month = months[date.month-1]
    return (f"{date.day} de {month} de {date.year}")
#verify the existence of the date
def checkIfTheDateExists(value):
    date = value.split("/")
    if int(date[2])%4==0 and int(date[2])%400 == 0:
        if int(date[1]) == 2:
            if date[0]==29:
                pass
            else:
                return "NULL"
    elif int(date[1]) == 2:
            if date[0]==28:
                pass
            else:
                return "NULL"
    if date[1] in [1,3,5,7,8,10,12] and date[0] > 31 or date[1] in [4,6,9,11] and date[0] > 30:
        return "NULL"
    return convertDate(int(date[2]),int(date[1]),int(date[0]))   
#start the process
dates = input("Enter with one dante using this format: dd/mm/aaaa: ")
print(f"The date converted is: {checkIfTheDateExists(dates)}")