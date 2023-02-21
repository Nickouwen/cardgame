from rest_framework import serializers

from ..models.game_model import Game


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    round_number = serializers.IntegerField(required=False)
    started_at = serializers.DateTimeField(required=False)
    status = serializers.CharField(max_length=1, required=False)

    def create(self, validated_data):
        return Game(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.round_number = validated_data.get(
            'round_number', instance.round_number)
        instance.status = validated_data.get('status', instance.status)
        return instance
