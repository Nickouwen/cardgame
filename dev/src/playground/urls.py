from django.urls import path

from . import apis

urlpatterns = [
    path('cards/', apis.card_list),
    path('cards/<int:id>/', apis.card_detail),
    path('game/create/', apis.create_game),
]
