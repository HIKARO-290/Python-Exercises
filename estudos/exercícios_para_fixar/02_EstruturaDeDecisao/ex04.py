# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# get the letter
letter = input("Enter with the letter: ")
#verify if the value is a one letter
if len(letter) > 1:
    print("You need enter with one letter")
#verify if the value is a number
elif letter.isnumeric():
    print("this is not a letter")
#verify if the letter is vowel or consonant
else:
    if letter in "aeiou":
        print("The letter is vowel")
    else:
        print("The letter is consonant")