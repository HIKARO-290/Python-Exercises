from math import ceil, floor
#get the size in megabytes from the archive you need to make the download
#pega o tamanho em megabytes do arquivo que precisa baixar
archive = float(input("Enter with the megabytes from the archive: "))
#get the velocity your internet has
#pega a velocidade sua internete possui
internet = float(input("Enter with the megabits your internet has"))
megabit = archive*8
#perform the calculus to time
#realiza calculo do tempo necessário
seconds = ceil((megabit/internet)%60)
minute = ceil((megabit/internet/60)%60)
hours = floor(megabit/internet/60/60)
#Show the value result
#Mostra o resultado
print(f"The time you need to make the download of this arquive is:\n {hours} hours\n {minute} minutes\n {seconds} seconds")