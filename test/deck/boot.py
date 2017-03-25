from deck import *

def main():
    d = Deck()
    d.create_boot()
    return d.shuffle_deck()
print(main())
