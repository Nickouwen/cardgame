"""
table.py
"""
from deck.card import Card
import random


class Table:

    def __init__(self):
        self.__cards: list[Card] = []
        self.__initialize_new_table()

    def __initialize_new_table(self):
        self.__cards.clear()
        for i in range(4):
            self.__cards.append(Card(random))
            print(Card)
