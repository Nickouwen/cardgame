from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cardgame.apis import CardgameAPI

from .serializers import GameSerializer
from .services.nics_game_service import NicsGameService

game_service = NicsGameService()


@api_view(['GET', 'POST'])
def game_list(request):
    if request.method == 'GET':
        serializer = GameSerializer(game_service._games, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        game_service._games.append(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
