"""
	At some point I will need to go in and make better var names.
"""

import json
from random import shuffle


class Deck(object):
    deck = []
    boot = []
    with open('card_config.json', 'r') as c:
        cards = json.load(c)

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

def begin_game():
    deck_num = 4
    d = Deck()
    d.create_boot(deck_num)
    return d.shuffle_deck()


def engine(boot):
	print("The dealer deals your cards. They are: {0} {1}".format(boot[0], boot[1]))
	boot.pop(0)
	boot.pop(0)
	print("The dealer deals your cards. They are: {0} {1}".format(boot[0], boot[1]))
	boot.pop(0)
	boot.pop(0)

engine(begin_game())
