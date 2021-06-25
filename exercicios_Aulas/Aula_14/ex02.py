#Faça um programa, com uma função que necessite de um argumento. A função retorna
#o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
#negativo e ‘0’ se for 0.
#define one function with one arg
def receiveOneArg(arg=""):
    if "n" in arg or "0" in arg:
        return "N"
    elif "p" in arg:
        return "P"
    else:
        return "error, invalid value!"
def receiveValuesFromUser():
    arg = str(input("Enter with positivo or negativo: ")).lower().strip(" ")
    return receiveOneArg(arg)
print("the response from the word you chose is:",receiveValuesFromUser())
