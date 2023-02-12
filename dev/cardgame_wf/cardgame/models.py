from django.db import models


# Create your models here.
class AbstractCardOwner(models.Model):
    class meta:
        abstract = True


class DeckModel(AbstractCardOwner):
    deck_name = models.CharField(max_length=255)


class PlayerModel(AbstractCardOwner):
    player_name = models.CharField(max_length=255)


class CardModel(models.Model):
    CLUBS = 'CL'
    DIAMONDS = 'DI'
    HEARTS = 'HE'
    SPADES = 'SP'
    NONE = ''
    SUIT_CHOICES = [
        (CLUBS, "Clubs"),
        (DIAMONDS, "Diamonds"),
        (HEARTS, "Hearts"),
        (SPADES, "Spades"),
        (NONE, ""),
    ]
    number = models.PositiveSmallIntegerField()
    suit = models.CharField(max_length=2, choices=SUIT_CHOICES, default=NONE)
    owner = models.ForeignKey(AbstractCardOwner, on_delete=models.PROTECT)
