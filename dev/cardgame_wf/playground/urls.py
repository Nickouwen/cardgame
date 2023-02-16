from django.urls import path

from . import views

urlpatterns = [
    path('cards/', views.card_list),
    path('cards/<int:id>/', views.card_detail),
    path('hello/', views.say_hello),
]
