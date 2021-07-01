# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula
# anterior, crie um lançador de dados e moedas em que o usuário deve
# escolher o objeto a ser lançado. Não esqueça que os lançamentos são
# feitos de forma randômica

from classes.dice import Dice
from classes.coin import Coin

class main:
    def makeChoise():
        name = input("Enter with your name: ")
        print("""Make one Choise:
        -1 roll dices
        -2 roll coin        
        """)
        if int(input("")) == 1:
            play = Dice(int(input("Enter with the number of side you tink: ")),name)
            print(play.verifyDecision(play.rollDice()))
        else:
            play = Coin(input("Enter with head or tail to try advice what coin side: "),name)
            print(play.verifyDecision(play.turnCoin()))
    makeChoise()