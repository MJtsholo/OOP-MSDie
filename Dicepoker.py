import random
import PokerApp
import Textinterface

inter = Textinterface()
app = PokerApp(inter)
app.run()

class Dice(object):
    def __init__(self):
        self.dice = []
        for i in range(5):
            self.dice.append(random.randint(1,6))
    def roll(self, indices):
        for i in indices:
            self.dice[i] = random.randint(1,6)
    def score(self):
        counts = [0, 0, 0, 0, 0, 0, 0]
        for i in self.dice:
            counts[i] += 1
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif 3 in counts and 2 in counts:
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0
        
class PokerApp(object):
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface
    
    def wantToPlay(self):
        ans = input("Do you wish to try your luck?")
        if ans[0].lower() == "y":
            return True
        else:
            return False
    
    def run(self):
        print ("You currently have %s." %self.money)
        while self.money >= 10 and self.interface.wantToPlay() == True:
            self.playRound()
            self.interface.close()
    
    def playRound(self):
        self.money -= 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        print ("%s. You win %s." %(result, score))
        self.money += score
        self.interface.setMoney(self.money)
        print ("You currently have $%s." %self.money)
    
    def doRolls(self):
        self.dice = Dice()
        rollCount = 1
        self.interface.setDice(self.dice.values())
        print ("Dice: %s" %self.dice.dice)
        toRoll = self.interface.chooseDice()
        while rollCount < 3 and toRoll != []:
            rollCount += 1
            self.dice.roll(toRoll)
            self.interface.setDice(self.dice.values())
            print ("Dice: %s" %self.dice.dice)
            if rollCount < 3:
                reRoll = input("Would you like to roll again?")
                if reRoll[0].lower() == "y":
                    toRoll = self.interface.chooseDice()
                else:
                    break

class TextInterface:
    def __init__(self):
        print('welcome to video poker')

    def setMoney(self, amt):
        print('you currently have ${0}.'.format(amt))

    def setDice(self, values):
        print('Dice:', values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck?")
        if ans[0].lower() == "y":
            return True

    def close(self):
        print('\nThanks for playing!')

    def showResult(self, msg, score):
        print("{O}. You win ${ 1}. " .format(msg, score ))

    def chooseDice(self):
        return eval(input('Enter list of which to change ([] to stop'))
          
game = PokerApp()
game.run()