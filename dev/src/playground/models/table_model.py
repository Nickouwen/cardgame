from .card_model import Card
from .cardcollection_model import CardCollection


def create_deck() -> CardCollection:
    # A CardCollection named deck
    cardcollection = CardCollection(name="Deck")

    # Create each card with the appropriate point value
    for i in range(1, 105):
        if i == 55:
            point_value = 7
        elif i % 11 == 0:
            point_value = 5
        elif i % 10 == 0:
            point_value = 3
        elif i % 5 == 0:
            point_value = 2
        else:
            point_value = 1
        cardcollection.cards[i] = Card(number=i, suit=Card.NONE,
                                       point_value=point_value)
    return cardcollection


class Table:
    def __init__(self) -> None:
        self.deck = create_deck()
        self.piles = []
        self.players = []

    def __str__(self) -> str:
        return f"Game {self.deck}"
