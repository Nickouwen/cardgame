from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .services import PlaygroundService


def say_hello(request):
    PlaygroundService.create_game(name="My New Game")

    return render(request, 'hello.html', {'name': 'Frans'})


@api_view()
def card_list(request):
    return Response('ok')


@api_view()
def card_detail(request, id):
    return Response(id)
