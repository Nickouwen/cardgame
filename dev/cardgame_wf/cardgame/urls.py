from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    path('hello', views.say_hello),
    path('api/v1/', include(router.urls))
]
