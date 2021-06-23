#gera dict com chaves
dictionary = {1:0,4:0,5:0,6:0,7:0,9:0}
#insere valor correspontende a valor da chave elevado a segunda potência
for i in dictionary.keys():
    dictionary[i]=i**2
#Exibe o valor do dicionário criado
print(dictionary) 