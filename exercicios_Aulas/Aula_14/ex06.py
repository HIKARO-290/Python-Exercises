#Escreva uma função que, dado um número nota representando a nota de um estudante,
#converte o valor de nota para um conceito (A, B, C, D, E e F)

#perform the conversion
def convertNote(note):
    if note >8.9:
        return "A"
    elif note >6.9:
        return "B"
    elif note >4.9:
        return "C"
    elif note >4.4:
        return "D"
    else:
        return "F"
#get the value from user
def getNote():
     note = float(input("Enter with the note from this student: "))
     return convertNote(note)
#show the reference result
print("The reference of the note from the student is:",getNote())