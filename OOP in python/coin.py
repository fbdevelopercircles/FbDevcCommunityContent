#using OOP to determine the side a coin is flipped to
#defining the module

import random

class Coin:
    #__init__ is the initializer method
    def __init__(self): 
        #we set the side facing up to be 'tails'
        self.sideup = 'Tail'
    
    #the toss method, flips the coin and get either a 'head' or 'tail' as the side up
    #the 'self' references the object properties to be inherited by the new method
    def toss(self):
        if random.randint (0,1) == 0:
            self.sideup = 'Tail'
        else:
            self.sideup = 'Head'
    
    #get_sideup method gets the value referenced by the self.sideup
    def get_sideup(self):
        return self.sideup
