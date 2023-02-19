from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cardgame.apis import CardgameAPI

from .services.nics_game_service import NicsGameService
from .services.services import PlaygroundService


def create_game(request):
    api = CardgameAPI(NicsGameService())
    game = api.create(game_name="My New Game")

    return render(request, 'game.html', {
        'id': game['id'],
        'name': game['name'],
        'round_number': game['round_number'],
        'started_at': game['started_at'],
        'status': game['status'],
    })


def game_detail(request, id):
    api = CardgameAPI(NicsGameService())
    game = api.get(game_id=id)

    if not game:
        return render(request, 'game.html')
    return render(request, 'game.html', {
        'id': game['id'],
        'name': game['name'],
        'round_number': game['round_number'],
        'started_at': game['started_at'],
        'status': game['status'],
    })


def update_game(request, id, name):
    api = CardgameAPI(NicsGameService())
    game = api.update(game_id=id, game_name=name)

    return render(request, 'game.html', {
        'id': game['id'],
        'name': game['name'],
        'round_number': game['round_number'],
        'started_at': game['started_at'],
        'status': game['status'],
    })


@api_view()
def delete_game(request, id):
    api = CardgameAPI(NicsGameService())
    success = api.delete(game_id=id)

    return Response(success)
