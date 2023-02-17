from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cardgame.models import Game, Table


def create_game(name):
    with transaction.atomic():
        game = Game()
        game.name = name
        game.save()

        table = Table()
        table.game = game
        table.save()


def update_game(id, new_name):
    Game.objects.filter(pk=id).update(name=new_name)


def delete_game(id):
    game = Game(pk=id)
    game.delete()


def say_hello(request):
    create_game("My New Game")

    return render(request, 'hello.html', {'name': 'Frans'})


@api_view()
def card_list(request):
    return Response('ok')


@api_view()
def card_detail(request, id):
    return Response(id)
