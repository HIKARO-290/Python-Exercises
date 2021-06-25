import os
import locale
from datetime import date, datetime 
os.system('cls' if os.name == 'nt' else 'clear')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#apply the conversion to date
def data(valor):    
# verify if date exist    
    if datetime.strptime(valor, '%d/%m/%Y'):
# return the converted date
        return datetime.strptime(valor, '%d/%m/%Y').date().strftime('%d/%B/%Y')
    else:
# if the date doesn't have a valid value return null
        return "NULL"

data = input("digite uma data no formato dd/mm/aaaa: ")
#show the result 
print(f"A data formatada é: {verificaValidade(data)}")