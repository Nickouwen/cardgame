from datetime import datetime


class Game:
    """
    Has an id, a name, a round_number, a started_at, and a status
    """
    STATUS_NEW = 'N'
    STATUS_INPROGRESS = 'I'
    STATUS_OVER = 'O'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New Game'),
        (STATUS_INPROGRESS, 'In Progress'),
        (STATUS_OVER, 'Game Over'),
    ]
    id = 1
    games = []

    def __init__(self, *, name: str) -> None:
        self.id = Game.id
        Game.id += 1
        self.name = name
        self.round_number = 0
        self.started_at = datetime.now()
        self.status = Game.STATUS_NEW
        Game.games.append(self)

    def __str__(self) -> str:
        return f"{self.name} - {[choice[1] for choice in Game.STATUS_CHOICES if choice[0] is self.status]}"


class Card:
    """
    Has an id, a number, a suit, and a point_value
    """
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
    id = 1
    cards = []

    def __init__(self, *, number: int, suit: str, point_value: int) -> None:
        self.id = Card.id
        Card.id += 1
        self.number = number
        self.suit = suit
        self.point_value = point_value
        Card.cards.append(self)

    def __str__(self) -> str:
        return f"({self.number}): {self.point_value} heads"


class CardCollection:
    """
    Has an id, a name, and card_ids
    """
    id = 1
    cardcollections = []

    def __init__(self, *, name: str = "New card collection") -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.name = name
        self.card_ids = []
        CardCollection.cardcollections.append(self)

    def __str__(self) -> str:
        return self.name


class Table:
    """
    Has an id and a game_id
    """
    id = 1
    tables = []

    def __init__(self, *, game_id: int) -> None:
        self.id = Table.id
        Table.id += 1
        self.game_id = game_id
        Table.tables.append(self)

    def __str__(self) -> str:
        return f"Game {self.game_id}"


class Player:
    """
    Has an id, a name, points, and a game_id
    """
    id = 1
    players = []

    def __init__(self, *, name: str, game_id: int) -> None:
        self.id = Player.id
        Player.id += 1
        self.name = name
        self.points = 0
        self.game_id = game_id
        Player.players.append(self)

    def __str__(self) -> str:
        return self.name


class TableCardCollection(CardCollection):
    """
    Has an id, a collection_id and a table_id
    """
    tablecardcollections = []

    def __init__(self, *, table_id: int, collection_id: int) -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.collection_id = collection_id
        self.table_id = table_id
        TableCardCollection.cardcollections.append(self)

    def __str__(self) -> str:
        return f"Collection {self.collection_id} at table {self.table_id}"


class PlayerCardCollection(CardCollection):
    """
    Has an id, a collection_id and a player_id
    """
    playercardcollections = []

    def __init__(self, *, collection_id: int, player_id: int) -> None:
        self.id = CardCollection.id
        CardCollection.id += 1
        self.collection_id = collection_id
        self.player_id = player_id
        PlayerCardCollection.playercardcollections.append(self)

    def __str__(self) -> str:
        return f"Collection {self.collection_id} of player {self.player_id}"
