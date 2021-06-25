import os
import locale
from datetime import date, datetime 
os.system('cls' if os.name == 'nt' else 'clear')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
def data(data2):
    try:
        data2 = datetime.strptime(data2, '%d/%m/%Y').date()
        dataFormatada = data2.strftime('%d/%B/%Y')
    except ValueError:
        return 'Data Inválida'
    else:
        return dataFormatada


data2 = input('Digite a data: ')
#dataFormatada = data(data2)
print(data(data2))