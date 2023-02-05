"""
deck.py
"""

import random
from dev.deck.card import Card


class Deck:
    """
    Class Deck
    """

    def __init__(self):
        self.cards: list(Card) = []
        self.initialize_new_deck()

    def initialize_new_deck(self):
        """
        Creates a new ordered deck
        :return:
        """
        self.cards.clear()
        for i in range(104):
            self.cards.append(Card(i + 1))

    def shuffle(self):
        """
        Randomizes the order of the cards in this deck
        :return:
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Removes a card from the beginning of the list and returns it
        :return: Card - the card drawn
        """
        card = self.cards.pop()
        return card
