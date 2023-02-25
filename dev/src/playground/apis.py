from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import (CardCollectionSerializer, CardSerializer,
                          GameSerializer, PlayerSerializer, TableSerializer)
from .services.nics_game_service import NicsGameService


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return NicsGameService()._games

    def get_object(self):
        obj = None
        for game in NicsGameService()._games:
            if game.id == int(self.kwargs['id']):
                obj = game
                break

        if not obj:
            raise Http404

        return obj


class TableViewSet(ModelViewSet):
    serializer_class = TableSerializer


class PlayerViewSet(ModelViewSet):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = None
        games = NicsGameService._games
        for game in games:
            if game.id == int(self.kwargs['game_id']):
                queryset = game.table.players
                break
        return queryset


class CardCollectionViewSet(ModelViewSet):
    serializer_class = CardCollectionSerializer


class CardViewSet(ModelViewSet):
    serializer_class = CardSerializer
