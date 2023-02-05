"""
hand.py
"""
from typing import Optional
from dev.deck.card import Card
from dev.deck.exception.card_not_found_error import CardNotFoundError


class Hand:
    """
    Class Hand
    """

    def __init__(self):
        self.__cards: list[Card] = []

    def add_card(self, card: Card):
        """
        :param card: Card to add to the hand
        :return: void
        """
        self.__cards.append(card)

    def get_hand(self) -> list[Card]:
        """
        :return: Cards in the hand
        """
        return self.__cards

    def play_card(self, number: int) -> Card:
        """
        :param number: The number of the card to play
        :raises: CardNotFoundError
        :return: The card if it's in the hand
        """
        result: Optional[Card] = None
        for card in self.__cards:
            if card.get_number() == number:
                result = card
                break
        if result is None:
            raise CardNotFoundError()
        self.__cards.remove(result)
        return result
