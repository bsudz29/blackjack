import random

class Card:
    face = {
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }
    chosen = set()
    def __init__(self):
        c = self.cardBuilder()
        self.rank = c[0]
        self.suit = c[1]
   
    def cardBuilder(self):
        rank = str(random.randint(2, 15))
        suit = random.choice("sdhc")
        create = rank + suit
        while create in self.chosen:
            rank = str(random.randint(2, 15))
            suit = random.choice("sdhc")
            create = rank + suit
        self.chosen.add(create)
        return (rank, suit)
        



