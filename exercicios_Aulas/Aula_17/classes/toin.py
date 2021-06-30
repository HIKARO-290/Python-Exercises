from random import randint
class Toin:
    def __init__(self,decision="head",name=""):
        self.playername = name
        self.sidehead = "head"
        self.sidetail = "tail"
        self.personaldecision = decision
    def turnCoin(self):
        coin = randint(2)
        if coin ==1:
            return self.sidehead
        else:
            return self.sidetail
    def verifyDecision(self,result):
        if self.personaldecision == result:
            return "You Win"
        else:
            return "You Lost"