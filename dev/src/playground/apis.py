from django.http import Http404
from rest_framework.viewsets import ModelViewSet

from .serializers import GameSerializer
from .services.nics_game_service import NicsGameService


class GameViewSet(ModelViewSet):
    queryset = NicsGameService()._games
    serializer_class = GameSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = None
        for game in NicsGameService()._games:
            if game.id == int(self.kwargs['id']):
                obj = game
                break

        if not obj:
            raise Http404

        return obj
