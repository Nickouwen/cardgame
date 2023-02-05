"""
card.py
"""


class Card:
    """
    Class Card
    """
    def __init__(self, card_number: int):
        self.card_number = card_number

    def __str__(self) -> str:
        return f"Card number: {self.card_number}"

    def set_card_number(self, card_number: int):
        """
        Sets the card number to the given number
        :param card_number: the number to set
        :return:
        """
        self.card_number = card_number

    def get_card_number(self) -> int:
        """
        Gets the current card number
        :return: int - card number
        """
        return self.card_number
