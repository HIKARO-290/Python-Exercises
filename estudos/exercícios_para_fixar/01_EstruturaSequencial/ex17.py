from math import ceil, floor
#get the value of the area to paint
#pega o valor da área a ser pintada
area = float(input("Enter with the size area: "))
#perform the calculus for 18 liters can
#realiza os calculos para latas de 18 litros
liters = area/6
caneighteen = ceil(liters/18)
allvalueeighteen = caneighteen * 80.00
#perform the calculus for 3.6 liters can
#realiza os calculos para latas de 3.6 litros
canthree = ceil(liters/3.6)
allvaluetheee = canthree * 25.00
#perform the calculus for mix  
#realiza os calculos para latas misturadas
canmixeighteen = floor(liters/18)
canmixthree=ceil((liters%18)/3.6)
allvaluemix = (canmixeighteen*80.00)+(canmixthree*25.00)
#Show the result values
#Mostra os valores resultantes
print(f"""
        The number of liters to paint this area is: {liters}
        
        The number of cans you need buy if use cans with 18 liters is: {caneighteen}
        The value you need to pay this cans is: {allvalueeighteen}

        The number of cans you need buy if use cans with 3.6 liters is: {canthree}
        The value you need to pay this cans is: {allvaluetheee}

        The number of cans you need buy if use one mix of cans is: 
                - from 18 can liters: {canmixeighteen}
                - from 3.6 can liters: {canmixthree}
        The value you need to pay this cans is: {allvaluemix}
        """)