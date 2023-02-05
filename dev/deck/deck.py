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
        self.__cards: list(Card) = []
        self.__initialize_new_deck()

    def __initialize_new_deck(self):
        self.__cards.clear()
        for i in range(104):
            self.__cards.append(Card(i + 1))

    def shuffle(self):
        """
        Randomizes the order of the cards in this deck
        :return: void
        """
        random.shuffle(self.__cards)

    def draw_card(self) -> Card:
        """
        Removes a card from the beginning of the list and returns it
        :return: The card drawn
        """
        card = self.__cards.pop()
        return card

    def peek_card(self) -> Card:
        """
        Shows the card at the top of the deck without drawing it
        :return: The card at the top of the deck
        """
        return self.__cards[len(self.__cards) - 1]
