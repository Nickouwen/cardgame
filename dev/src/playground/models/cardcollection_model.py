class CardCollection:
    def __init__(self, name: str = "New card collection") -> None:
        self.name = name
        self.cards = dict()  # Dictionary: Key = int, value = Card

    def __str__(self) -> str:
        return self.name
