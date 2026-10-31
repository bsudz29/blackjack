import random
import pandas as pd
class Card:
    deck = pd.read_csv('cards.csv') 
    chosen = set()
    print(chosen) 
   
    def __init__(self):
        num = random.randint(0, 51)
        while num in Card.chosen: #!potential issue when all cards are drawn
            num = random.randint(0, 51)
        Card.chosen.add(num)
        c = Card.deck.iloc[num]
        self._rank = c.iloc[0]
        self._suit = c.iloc[1]
        self._image = c.iloc[2]
            
    @property
    def getSuit(self):
        return self._suit
    @property
    def getRank(self):
        return self._rank
    @property
    def getImage(self):
        return self._image
        



