import json
from random import shuffle

class Card(object):
    def __init__(self):
        with open('card_config.json', 'r') as c:
            cards = json.load(c)

            for suit in cards["suits"]:
                for rank in cards["ranks"]:
                    deck.append(rank + suit)

'''
    Creates the boot that cards are dealt from.
'''
class Boot(object):
    deck = []
    '''with open('card_config.json', 'r') as c:
        cards = json.load(c)

    for suit in cards["suits"]:
        for rank in cards["ranks"]:
            deck.append(rank + suit)'''
    def __init__(self):
            self.deck = Card()

    def create_boot(self, num):
        #num is the number of decks in the boot
        self.boot = self.deck * num

        return self.boot

    def shuffle_boot(self):
        x = self.boot
        shuffle(x)
        return x


def begin_game():
    d = Boot()
    d.create_boot(4)
    return d.shuffle_boot()


def engine(boot):
    print("The dealer deals your cards. They are: {0} {1}".format(boot[0], boot[1]))
    boot.pop(0)
    boot.pop(0)
    print("The dealer deals her cards. They are: {0} {1}".format(boot[0], boot[1]))
    boot.pop(0)
    boot.pop(0)

engine(begin_game())
