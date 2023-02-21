from rest_framework import routers

from . import apis

router = routers.DefaultRouter()
router.register('games', apis.GameViewSet, basename='game')

urlpatterns = router.urls
