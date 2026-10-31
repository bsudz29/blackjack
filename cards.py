import random
import pandas as pd
class Card:
    deck = pd.read_csv('cards.csv') 
    chosen = set()
   
    def __init__(self):
        pass

    def build(self):
        index = random.randint(0, 52)
        selected = deck.iloc[index]
        
    
    @property
    def getSuit(self):
        pass
    @property
    def getRank(self):
        pass
    @property
    def getImage(self):
        pass
        



