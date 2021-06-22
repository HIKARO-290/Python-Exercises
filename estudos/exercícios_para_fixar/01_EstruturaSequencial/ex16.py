from math import ceil
#get the value of the area to paint
#pega o valor da área a ser pintada
area = float(input("Enter with the size area: "))
#perform the calculus
#realiza os calculos
liters = area/3
can = ceil(liters/18)
allvalue = can * 80.00
#Show the result values
#Mostra os valores resultantes
print(f"""
        The number of liters to paint this area is: {liters}
        The number of cans you need to paint is: {can}
        The value you need to pay this cans is: {allvalue}
        """)