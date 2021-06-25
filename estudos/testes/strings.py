# teste = "uma String pAra testes   "
# print(teste)
# print(f"{teste.lower()}")
# print(f"{teste.upper()}")
# print(f"{teste[::-1]}")
# print(f"{teste[1]}")
# print(f"{teste[1:5]}")
# print(f"{teste.title()}")
# print(f"{teste.capitalize()}")
# print(f"{teste.swapcase()}")
# print(f"{teste.ljust(50)}")
# print(f"{teste.split(' ')}")
# print(f"{teste.replace('String','batata')}")
# print(f"{teste.strip()}")
# print(f"{teste.center(50)}")
# print(f"{teste.find('r')}")
# print(f"{teste.startswith('u')}")
# print(f"{teste.endswith('s')}")
# print(f"{teste.islower()}")
# print(f"{teste.isupper()}")
# print(f"{type(teste)}")
# print(f"{teste.count('a')}")
# print(f"{len(teste)}")



# listacomp = [["and","gab"],["luc","ant"],["lima","part"]]
# print((listacomp[1][0]))
lista = {
    'nome':'hikaro',
    'Nota': float(5.5)
} 
print("".ljust(33).replace(" ","_")) 
print("|"+"TABELA".center(37-len("TABELA"))+"|")  
print("|".ljust(32).replace(" ","_")+"|") 
for i,t in lista.items():
    print(f"|{str(i).ljust(15)}|{str(t).ljust(15)}|")
    
    


    