"""
Rudimentary build of a blackjack game. Soon to be, hopefully, a sweet build of a blackjack
game.

I keep saying I'm going to write better variable names, and I never do...

"""
import json
from random import shuffle

class Hand(object):
    def __init__(self, card0, card1):
        self.card0 = card0[:-1]
        self.card1 = card1[:-1]
        
    def set_card_value(self, card):
        if card in "123456789":
            card_value = int(card)
        elif card in ["10", "J", "Q", "K"]:
            card_value = 10
        else:
            card_value =  11
        
        return card_value
        
    def calc_hand_value(self):
       self.hand_value =  self.set_card_value(self.card0) + self.set_card_value(self.card1)
    
"""
    Creates the boot that cards are dealt from.
"""
class Boot(object):
    deck = []
    with open('card_config.json', 'r') as c:
        cards = json.load(c)

    for suit in cards["suits"]:
        for rank in cards["ranks"]:
            deck.append(rank + suit)


    def create_boot(self, num):
        #num is the number of decks in the boot
        self.deck = self.deck * num

        return self.deck

    def shuffle_boot(self):
        x = self.deck
        shuffle(x)
        return x


def begin_game():
    d = Boot()
    d.create_boot(4)
    return d.shuffle_boot()
    
def get_hand_value(card0, card1):
    h = Hand(card0, card1)
    h.calc_hand_value()
    return h.hand_value
    
def engine(boot):
    print("The dealer deals your cards. They are: {0} {1}".format(boot[0], boot[1]))
    print("And the value of the hand is: {0}".format(get_hand_value(boot[0], boot[1])))
    boot.pop(0)
    boot.pop(0)
    print("The dealer deals her cards. They are: {0} {1}".format(boot[0], boot[1]))
    print("And the value of the hand is: {0}".format(get_hand_value(boot[0], boot[1])))
    boot.pop(0)
    boot.pop(0)

engine(begin_game())
