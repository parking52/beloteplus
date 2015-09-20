from deck import Deck
import random
from order import Order
order = Order()

class Game:

    def __init__(self, player_1, player_2, player_3, player_4, deck):

        self.loot_team_1 = []
        self.bonus_value_team_1 = 0
        self.loot_team_2 = []
        self.bonus_value_team_2 = 0

        self.deal(player_1, player_2, player_3, player_4, deck)
        self.set_trump(deck, "Spade")
        self.deal(player_1, player_2, player_3, player_4, deck)
        self.check_for_belote(player_1, player_2, player_3, player_4)

        print(" ------- Game On -------")
        for i in range(1, 9):
            self.state = []
            self.add_card_to_state(player_1)
            self.add_card_to_state(player_2)
            self.add_card_to_state(player_3)
            self.add_card_to_state(player_4)

            print("---------- state " + str(i) + "  ----------")
            self.display_state()

            winning_player_position = self.resolve_state()
            if winning_player_position == 1 or winning_player_position == 3:
                for card in self.state:
                    self.loot_team_1.append(card)
            else:
                for card in self.state:
                    self.loot_team_2.append(card)

        if winning_player_position == 1 or winning_player_position == 3:
            self.bonus_value_team_1 += + 10
        else:
            self.bonus_value_team_2 += + 10

        self.display_loot()

    def resolve_state(self):

        if order.compare_cards_is_bigger(self.state[0], self.state[1]):
            if order.compare_cards_is_bigger(self.state[0], self.state[2]):
                if order.compare_cards_is_bigger(self.state[0], self.state[3]):
                    return 1
                else:
                    return 4
            else:
                if order.compare_cards_is_bigger(self.state[2], self.state[3]):
                    return 3
                else:
                    return 4
        else:
            if order.compare_cards_is_bigger(self.state[1], self.state[2]):
                if order.compare_cards_is_bigger(self.state[1], self.state[3]):
                    return 2
                else:
                    return 4
            else:
                if order.compare_cards_is_bigger(self.state[2], self.state[3]):
                    return 3
                else:
                    return 4

    def add_card_to_state(self, player):
        self.state.append(player.play_card(random.randint(0, len(player.cards)-1)))
        # self.state.append(player.play_card(0))

    def deal(self, player_1, player_2, player_3, player_4, deck):

        player_1.get_cards(deck)
        player_2.get_cards(deck)
        player_3.get_cards(deck)
        player_4.get_cards(deck)

    def set_trump(self, deck, trump_color):

        deck.set_trump(trump_color)

    def display_state(self):
        for card in self.state:
            print(card.value, card.color)

    def check_for_belote(self, player_1, player_2, player_3, player_4):
        for player in [player_1, player_2, player_3, player_4]:
            pair = 0
            for card in player.cards:
                if card.trump and (card.value == 12 or card.value == 13):
                    pair += 1
            if pair == 2:
                if player.player_position == 1 or player.player_position == 3:
                    self.bonus_value_team_1 += 20
                else:
                    self.bonus_value_team_2 += 20



    def display_loot(self):

        print("------- Results & Loots -------")
        # print("Loot Team 1")
        #
        # for card in self.loot_team_1:
        #     print(card.value, card.color)
        #
        # print("Loot Team 2")
        #
        # for card in self.loot_team_2:
        #     print(card.value, card.color)

        print("Value Team 1: " + str(order.compute_value(self.loot_team_1) + self.bonus_value_team_1))
        print("Value Team 2: " + str(order.compute_value(self.loot_team_2) + self.bonus_value_team_2))
