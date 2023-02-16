"""
player.py
"""
from ..deck.hand import Hand


class Player:
    """
    Class Player
    """
    def __init__(self):
        self.__hand: Hand = Hand()

    """
    def give_card(self, card: Card):

    def play_card(self, number: int) -> Card:
    """
