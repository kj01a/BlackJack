from boot2 import *
from sys import exit

class Player(object): # The player.
	
	def __init__(self):
		pass
	
	def hit(self):
		pass
	
	def stand(self):
		exit(0)
	
	def split(self):
		pass
	
	def double_down(self):
		pass
	
	def bet(self):
		pass
	
	def surrender(self):
		pass
	
	def enter(self):
		
		choice = input("Do you want to play? Y/N? ").lower()
	
		if choice == "y":
			engine(begin_game())
			print(d.boot)
			
		else:
			exit(0)
	
	def leave(self):
		pass
		
	def play_move(self):
		pass
"""
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
"""		
		
p = Player()

p.enter()


