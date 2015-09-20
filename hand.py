from card import Card
from deck import Deck

class Hand():

    def __init__(self, name, player_position):
        self.cards = []
        self.name = name
        self.player_position = player_position

    def play_card(self, i):
        return self.cards.pop(i)

    def display_hand(self):
        for card in self.cards:
            print(card.value, card.color)

    def empty_the_hand(self):
        self.cards = []

    def get_cards(self, deck):
        self.empty_the_hand()
        self.cards.append(deck.deck[(self.player_position-1)*3])
        self.cards.append(deck.deck[(self.player_position-1)*3+1])
        self.cards.append(deck.deck[(self.player_position-1)*3+2])
        self.cards.append(deck.deck[(self.player_position-1)*2+12])
        self.cards.append(deck.deck[(self.player_position-1)*2+13])
        self.cards.append(deck.deck[(self.player_position-1)*3+20])
        self.cards.append(deck.deck[(self.player_position-1)*3+21])
        self.cards.append(deck.deck[(self.player_position-1)*3+22])

