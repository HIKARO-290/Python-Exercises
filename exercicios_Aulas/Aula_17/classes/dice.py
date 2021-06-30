from random import randint
class Dice:
    def __init__(self,side=0,name=""):
        self.playername = name
        self.sidedice = side
    def rollDice(self):
        return randint(1,6)
    def verifyDecision(self,value):
        if value == self.sidedice:
            return "You Win!!" 
        else:
            return "You Lost"
