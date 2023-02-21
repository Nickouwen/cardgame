from django.urls import path

from . import apis

urlpatterns = [
    path('games/', apis.game_list),
]
