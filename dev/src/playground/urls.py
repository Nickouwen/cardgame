from django.urls import path

from . import apis

urlpatterns = [
    path('cards/', apis.card_list),
    path('cards/<int:id>/', apis.card_detail),
    path('hello/', apis.say_hello),
]
