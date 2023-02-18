"""
card.py
"""


class Card:
    """
    Class Card
    """

    def __init__(self, number: int = 1):
        if number < 1 or number > 104:
            raise ValueError("Number must be between 1 and 104")
        self.__number = number

    def __str__(self) -> str:
        return f"Card number: {self.__number}"

    def set_number(self, number: int):
        """
        :param number: Number to set between 1 and 104
        :raises ValueError: Number is not between 1 and 104
        :return: void
        """
        if number < 1 or number > 104:
            raise ValueError("Number must be between 1 and 104")
        self.__number = number

    def get_number(self) -> int:
        """
        :return: Card number
        """
        return self.__number
