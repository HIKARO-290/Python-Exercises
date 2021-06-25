# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
#get the sex type
sex = input("Enter with your sex type: ")
# verify the response
if sex.lower().strip(" ").startswith('f'):
    print("the sex from user is female")
elif sex.lower().strip(" ").startswith('m'):
    print("the sex from user is male")
else:
    print("undefined sex")