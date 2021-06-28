# Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
firstnote = float(input("Enter with the first note: "))
secondnote = float(input("Enter with the second note: "))
middle = (firstnote + secondnote) / 2
if middle == 10:
    print("Congratulations you have passed with distintion!! Your note is:",middle)
elif middle >=7:
    print("You have pass with",middle,"like your note!")
elif middle <7:
    print("You have REPROVED with",middle,"like your note!")
else:
    print("Some note has an incorrect value!")