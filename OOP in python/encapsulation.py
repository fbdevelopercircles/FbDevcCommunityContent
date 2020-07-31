#making sideup method private (Encapsulation)
#data attributes are made private so that only the object’s methods can directly access them
import random

class Coin:
    #__init__ is the initializer method
    def __init__(self): 
        #we set the side facing up to be 'tails'
        #the __ indicates that sideup is a private data attribute
        self.__sideup = 'Tail'
    
    #the toss method, flips the coin and get either a 'head' or 'tail' as the side up
    #the 'self' references the object properties to be inherited by the new method
    def toss(self):
        if random.randint (0,1) == 0:
            self.__sideup = 'Tail'
        else:
            self.__sideup = 'Head'
    
    #get_sideup method gets the value referenced by the self.sideup
    def get_sideup(self):
        return self.__sideup
    
def main():
    #create an object for the class Coin
    a_coin = Coin()

    #identify the side facing up
    up_side = a_coin.get_sideup()
    print('the side facing up is:', up_side)

    #let's toss the coin
    print('flipping the coin, i get:')
    a_coin.toss()
  
    print(a_coin.get_sideup())
    
    #the code below does not over write the 'a_coin.toss()' method, 
    #infact the coin gets tossed because the 'self.__sideup' is private
    a_coin.sideup  = 'Head'
    print('i set the side up to be ', a_coin.get_sideup())

main()
