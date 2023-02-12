from django.shortcuts import render
from django.http import HttpRequest
from rest_framework import viewsets

from .models import CardModel
from .serializers import CardSerializer


# Create your views here.
def say_hello(request: HttpRequest):
    return render(request, 'hello.html', {'name': 'Frans'})


class CardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer
