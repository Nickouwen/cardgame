from rest_framework import serializers

from ..models.game_model import Game
from ..services.nics_game_service import NicsGameService


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=255)
    round_number = serializers.IntegerField(required=False)
    started_at = serializers.DateTimeField(required=False)
    status = serializers.CharField(max_length=1, required=False)

    def create(self, validated_data):
        name = validated_data['name']
        return NicsGameService().create_game(name)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.round_number = validated_data.get(
            'round_number', instance.round_number)
        instance.status = validated_data.get('status', instance.status)
        return instance
