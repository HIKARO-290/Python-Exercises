import random
tupla = tuple()
for cont in range(5):
    tupla += tuple([random.randrange(1,50)])

print(tupla)

print(f"o menor valor é : {min(tupla)} o maior valor é {max(tupla)}")