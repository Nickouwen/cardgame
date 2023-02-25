from rest_framework import serializers

from .services.nics_game_service import NicsGameService


class CardSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    suit = serializers.CharField()
    point_value = serializers.IntegerField()


class CardCollectionSerializer(serializers.Serializer):
    name = serializers.CharField()
    cards = serializers.DictField(child=CardSerializer())


class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField()
    hand = CardCollectionSerializer()
    points = serializers.IntegerField()


class TableSerializer(serializers.Serializer):
    deck = CardCollectionSerializer()
    piles = CardCollectionSerializer(many=True)
    players = PlayerSerializer(many=True)


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    table = TableSerializer(read_only=True)
    round_number = serializers.IntegerField(read_only=True)
    started_at = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)

    def create(self, validated_data):
        name = validated_data['name']
        return NicsGameService().create_game(name)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.round_number = validated_data.get(
            'round_number', instance.round_number)
        instance.status = validated_data.get('status', instance.status)
        return instance
