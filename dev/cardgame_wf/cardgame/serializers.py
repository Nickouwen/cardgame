from rest_framework import serializers

from .models import CardModel, DeckModel, PlayerModel


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeckModel
        fields = ["deck_name"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        field = ["player_name"]


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = ["number", "suit", "owner"]
