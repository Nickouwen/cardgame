from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cardgame.apis import CardgameAPI

from .services.nics_game_service import NicsGameService
from .services.services import PlaygroundService


def create_game(request):
    api = CardgameAPI(NicsGameService())
    game = api.create(game_name="My New Game")

    return render(request, 'hello.html', {
        'id': game['id'],
        'name': game['name'],
        'round_number': game['round_number'],
        'started_at': game['started_at'],
        'status': game['status'],
    })


def game_detail(request, id):
    api = CardgameAPI(NicsGameService())
    game = api.get(game_id=int(id))

    return render(request, 'hello.html', {
        'id': game['id'],
        'name': game['name'],
        'round_number': game['round_number'],
        'started_at': game['started_at'],
        'status': game['status'],
    })


@api_view()
def card_list(request):
    return Response('ok')


@api_view()
def card_detail(request, id):
    return Response(id)
