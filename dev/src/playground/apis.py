from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cardgame.apis import CardgameAPI

from .serializers import GameSerializer
from .services.nics_game_service import NicsGameService


@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        games = NicsGameService.get_all_games()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
