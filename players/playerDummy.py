from card import Card
from deck import Deck
from players.interface_player import Hand


class PlayerDummy(Hand):

    def __init__(self, name, player_position):
        super().__init__(name, player_position)

    def play_card(self, state):
        return self.cards.pop(0)
