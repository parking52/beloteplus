from deck import Deck
from hand import Hand
from order import Order
from game import Game

deck = Deck()
order = Order()

# Shuffle Deck
# deck.shuffle()
# deck.display_deck()

# Set players
player_1 = Hand("player_1", 1)
player_2 = Hand("player_2", 2)
player_3 = Hand("player_3", 3)
player_4 = Hand("player_4", 4)

# Game start
game = Game(player_1, player_2, player_3, player_4, deck)






