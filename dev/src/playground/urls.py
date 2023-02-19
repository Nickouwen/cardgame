from django.urls import path

from . import apis

urlpatterns = [
    path('game/create/', apis.create_game),
    path('game/<int:id>/', apis.game_detail),
    path('game/update/<int:id>/<name>', apis.update_game),
    path('game/delete/<int:id>/', apis.delete_game),
]
