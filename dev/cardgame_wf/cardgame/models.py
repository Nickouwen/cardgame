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


class CardCollection(models.Model):
    pass


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
    suit = models.CharField(max_length=1, choices=SUIT_CHOICES, default=NONE)
    point_value = models.PositiveSmallIntegerField()
    collection = models.ForeignKey(
        CardCollection, on_delete=models.PROTECT, null=True, default=None)


class Table(models.Model):
    game = models.OneToOneField(
        Game, on_delete=models.CASCADE, primary_key=True)


class Player(models.Model):
    name = models.CharField(max_length=255)
    points = models.PositiveSmallIntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class TableCardCollection(models.Model):
    collection = models.OneToOneField(
        CardCollection, on_delete=models.CASCADE, primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)


class PlayerCardCollection(models.Model):
    name = models.CharField(max_length=255)
    collection = models.OneToOneField(
        CardCollection, on_delete=models.CASCADE, primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
