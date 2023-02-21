from .cardcollection_model import CardCollection


class Player:
    def __init__(self, name: str) -> None:
        self.hand = CardCollection("Hand")
        self.name = name
        self.points = 0

    def __str__(self) -> str:
        return self.name
