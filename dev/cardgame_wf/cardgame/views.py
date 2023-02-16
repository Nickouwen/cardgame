from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def card_list(request):
    return Response('ok')


@api_view()
def card_detail(request, id):
    return Response(id)
