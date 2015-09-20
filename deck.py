from card import Card
import random

class Deck():

    def __init__(self):
        self.deck = []
        self.deck.append(Card(7, "Heart"))
        self.deck.append(Card(8, "Heart"))
        self.deck.append(Card(9, "Heart"))
        self.deck.append(Card(10, "Heart"))
        self.deck.append(Card(11, "Heart"))
        self.deck.append(Card(12, "Heart"))
        self.deck.append(Card(13, "Heart"))
        self.deck.append(Card(14, "Heart"))

        self.deck.append(Card(7, "Diamond"))
        self.deck.append(Card(8, "Diamond"))
        self.deck.append(Card(9, "Diamond"))
        self.deck.append(Card(10, "Diamond"))
        self.deck.append(Card(11, "Diamond"))
        self.deck.append(Card(12, "Diamond"))
        self.deck.append(Card(13, "Diamond"))
        self.deck.append(Card(14, "Diamond"))

        self.deck.append(Card(7, "Spade"))
        self.deck.append(Card(8, "Spade"))
        self.deck.append(Card(9, "Spade"))
        self.deck.append(Card(10, "Spade"))
        self.deck.append(Card(11, "Spade"))
        self.deck.append(Card(12, "Spade"))
        self.deck.append(Card(13, "Spade"))
        self.deck.append(Card(14, "Spade"))

        self.deck.append(Card(7, "Club"))
        self.deck.append(Card(8, "Club"))
        self.deck.append(Card(9, "Club"))
        self.deck.append(Card(10, "Club"))
        self.deck.append(Card(11, "Club"))
        self.deck.append(Card(12, "Club"))
        self.deck.append(Card(13, "Club"))
        self.deck.append(Card(14, "Club"))

    def shuffle(self):
        random.shuffle(self.deck)

    def display_deck(self):
        for card in self.deck:
            print(card.value, card.color)

    def set_trump(self, card_color):
        for card in self.deck:
            if card.color == card_color:
                card.trump = True
            else:
                card.trump = False