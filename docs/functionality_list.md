#Funtionality

##Game
  + Plays blackjack
    - Hit, Stand, Double Down, Split, & Surrender
    - Option for insurance when Dealer is a Ace
    - Dealer stands on a soft 17
    - Player win pays 1:1 on a normal win & 3:2 on blackjack
  + Player starts with a certain number of chips and able to place bets from that pool 
  + The game determines the best move based on [basic startegy](https://en.wikipedia.org/wiki/Blackjack#Basic_strategy). **KJ**
    -Logic for double down
  + The keeps the [count](https://en.wikipedia.org/wiki/Card_counting) of the boot, based on the Hi-Lo system, and determines whether or not the basic strategy play is best, and if not, which play is better. **KJ**
  
##Statistics engine
  (Curt please fill in whatever you want.)
  + Automate gameplay
  + Calculate dealers advantage
  + Calculate difference in when using only basic strategy vs counting
  + Input all data into a sql database
  + Use matplotlib to generate visual reports
  
##GUI
  + Show cards
  + Show players bet
  + Show players chip pool 
  
##Advanced
  + Turn into a fully installable linux application, utilizing distutils and the setup.py
  + Utilize the PyGame framework
  + Utilize NumPy framework
