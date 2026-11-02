import random
import pandas as pd
class Card:
    deck = pd.read_csv('cards.csv') 
    chosen = set()
   
    def __init__(self):
        num = random.randint(0, 51)
        while num in Card.chosen: 
            num = random.randint(0, 51)
        Card.chosen.add(num)
        c = Card.deck.iloc[num]
        self._rank = c.iloc[0]
        self._suit = c.iloc[1]
        self._image = c.iloc[2]
        
        #ace value of 1 logic will be implemented with the setter
        if self._rank == 'Ace':
            self._value = 11
        elif self._rank in ['Jack', 'Queen', 'King']:
            self._value = 10
        else:
            self._value = int(c.iloc[0])
            
    @property
    def getSuit(self):
        return self._suit
    @property
    def getRank(self):
        return self._rank
    @property
    def getImage(self):
        return self._image

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new): #right now only to be used to set ace to value: 1 when applies
        self._value = new
        