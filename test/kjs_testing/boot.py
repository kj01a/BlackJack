"""
Rudimentary build of a blackjack game. Soon to be, hopefully, a sweet build of a blackjack
game.

I keep saying I'm going to write better variable names, and I never do...

"""
import json
from random import shuffle

class Card(object):
    def __init__(self, card):
        self.card = card[:-1]
        self.card_value = card
        
    def set_card_values(self):
        if self.card in "123456789":
            self.card_value = int(self.card)
        elif self.card in ["10", "J", "Q", "K"]:
            self.card_value = 10
        else:
            self.card_value =  11
            
    def get_card_values(self):
        return self.card_value
    
'''
    Creates the boot that cards are dealt from.
'''
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
    
def calc_hand_value(card0, card1):
    hand_value = 0
    first_card = Card(card0)
    second_card = Card(card1)
    
    first_card.set_card_values()
    second_card.set_card_values()
    
    hand_value = first_card.card_value + second_card.card_value
    
    print("And the value of the hand is: {0}".format(hand_value))
    
def engine(boot):
    print("The dealer deals your cards. They are: {0} {1}".format(boot[0], boot[1]))
    calc_hand_value(boot[0], boot[1])
    boot.pop(0)
    boot.pop(0)
    print("The dealer deals her cards. They are: {0} {1}".format(boot[0], boot[1]))
    calc_hand_value(boot[0], boot[1])
    boot.pop(0)
    boot.pop(0)

engine(begin_game())
