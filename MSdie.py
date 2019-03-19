import random
class MSDie(object):
    
    
    #construct here
    #define classmethod 'roll' to roll the MSdie
    #I used 'dieroll' to roll the die
    def __init__(self):
        self.dieside = 6
        self.dieroll()
    
    
    def dieroll(self):
        self.value= 1 + random.randrange(self.dieside)
        return self.value
    
    #define classmethod 'getValue' to return the current value of the MSdie
    def getValue( self ):
        return self.value
    

#define classmethod 'setValue' to set the die to a particular value
def main():
    #d1, d2 = d2, d1
    d1 = MSDie()
    #d1 = MSDie()
    #d2 = MSDie()
    for n in range(1):
         #print (d1.dieroll(), d2.dieroll)
        print(d1.dieroll())
        


main()