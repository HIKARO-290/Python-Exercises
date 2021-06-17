import random
numero = ""
for i in range(5):
    numero += str(random.randrange(1,50)) 
    if i < 4:
        numero += ","
tupla = (numero)
print(tupla)

print(f"o menor valor é : {min(tupla)} o maior valor é {max(tupla)}")