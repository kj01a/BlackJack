"""
	At some point I will need to go in and make var names.
"""

import json
from random import shuffle


class Deck(object):
    def __init__(self):
        self.deck = []
        self.boot = []
        with open('card_config.json', 'r') as c:
            self.cards = json.load(c)

    def create_deck(self):
        for suit in self.cards["suits"]:
            for rank in self.cards["ranks"]:
                self.deck.append(rank + suit)

        return self.deck


    def create_boot(self, num):
        #num is the number of decks in the boot
        for x in range(num):
            for i in self.create_deck():
                self.boot.append(i)

        return self.boot

    def shuffle_deck(self):
        x = self.boot
        shuffle(x)
        return x

deck_num = int(input("How many decks will you use? "))
d = Deck()
d.create_boot(deck_num)
print(d.shuffle_deck())
