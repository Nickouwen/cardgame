from datetime import datetime


class Game:
    STATUS_NEW = 'N'
    STATUS_INPROGRESS = 'I'
    STATUS_OVER = 'O'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New Game'),
        (STATUS_INPROGRESS, 'In Progress'),
        (STATUS_OVER, 'Game Over'),
    ]
    id = 0

    def __init__(self) -> None:
        self.id = Game.id
        Game.id += 1
        self.name = ''
        self.round_number = 0
        self.started_at = datetime.now()
        self.status = Game.STATUS_NEW

    def __str__(self) -> str:
        return f"{self.name} - {[choice[1] for choice in Game.STATUS_CHOICES if choice[0] is self.status]}"


class Card:
    CLUBS = 'C'
    DIAMONDS = 'D'
    HEARTS = 'H'
    SPADES = 'S'
    NONE = ''
    SUIT_CHOICES = [
        (CLUBS, "Clubs"),
        (DIAMONDS, "Diamonds"),
        (HEARTS, "Hearts"),
        (SPADES, "Spades"),
        (NONE, ""),
    ]
    id = 0

    def __init__(self) -> None:
        self.id = Card.id
        Card.id += 1
        self.number = 1
        self.suit = Card.NONE
        self.point_value = 1

    def __str__(self) -> str:
        return f"({self.number}): {self.point_value} heads"


class CardCollection:
    id = 0

    def __init__(self) -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.name = "New Collection"
        self.cards = None

    def __str__(self) -> str:
        return self.name


class Table:
    id = 0

    def __init__(self) -> None:
        self.id = Table.id
        Table.id += 1
        self.game = Game()

    def __str__(self) -> str:
        return f"{self.game}"


class Player:
    id = 0

    def __init__(self) -> None:
        self.id = Player.id
        Player.id += 1
        self.name = ""
        self.points = 0
        self.game = Game()

    def __str__(self) -> str:
        return self.name


class TableCardCollection(CardCollection):
    def __init__(self) -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.collection = CardCollection()
        self.table = Table()

    def __str__(self) -> str:
        return f"{self.collection} at table {self.table}"


class PlayerCardCollection(CardCollection):
    def __init__(self) -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.collection = CardCollection()
        self.player = Player()

    def __str__(self) -> str:
        return f"{self.collection} of player {self.player}"
