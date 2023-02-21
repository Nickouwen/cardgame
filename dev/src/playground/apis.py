from rest_framework.viewsets import ModelViewSet

from .serializers import GameSerializer
from .services.nics_game_service import NicsGameService


class GameViewSet(ModelViewSet):
    queryset = NicsGameService()._games
    serializer_class = GameSerializer
