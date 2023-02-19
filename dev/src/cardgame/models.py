from django.db import models


class Game(models.Model):
    STATUS_NEW = 'N'
    STATUS_INPROGRESS = 'I'
    STATUS_OVER = 'O'
    STATUS_CHOICES = [
        (STATUS_NEW, 'New Game'),
        (STATUS_INPROGRESS, 'In Progress'),
        (STATUS_OVER, 'Game Over'),
    ]
    name = models.CharField(max_length=255)
    round_number = models.PositiveSmallIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_NEW)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
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
    number = models.PositiveSmallIntegerField()
    suit = models.CharField(
        max_length=1, choices=SUIT_CHOICES, blank=True, default=NONE)
    point_value = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return f"({self.number}): {self.point_value} heads"


class CardCollection(models.Model):
    name = models.CharField(max_length=255, default="New Collection")
    cards = models.ManyToManyField(
        Card, blank=True, default=None)

    def __str__(self) -> str:
        return self.name


class Table(models.Model):
    game = models.OneToOneField(
        Game, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f"{self.game}"


class Player(models.Model):
    name = models.CharField(max_length=255)
    points = models.PositiveSmallIntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class TableCardCollection(models.Model):
    collection = models.OneToOneField(
        CardCollection, on_delete=models.CASCADE, primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.collection} at table {self.table}"


class PlayerCardCollection(models.Model):
    collection = models.OneToOneField(
        CardCollection, on_delete=models.CASCADE, primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.collection} of player {self.player}"
