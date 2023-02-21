class Card:
    CLUBS = 'C'
    DIAMONDS = 'D'
    HEARTS = 'H'
    SPADES = 'S'
    NONE = 'N'
    SUIT_CHOICES = [
        (CLUBS, "Clubs"),
        (DIAMONDS, "Diamonds"),
        (HEARTS, "Hearts"),
        (SPADES, "Spades"),
        (NONE, ""),
    ]

    def __init__(self, *, number: int, suit: str, point_value: int) -> None:
        self.number = number
        self.suit = suit
        self.point_value = point_value

    def __str__(self) -> str:
        return f"({self.number}): {self.point_value} points"
