from rest_framework_nested import routers

from . import apis

router = routers.DefaultRouter()
router.register('games', apis.GameViewSet, basename='games')

games_router = routers.NestedDefaultRouter(router, 'games', lookup='game')
games_router.register('players', apis.PlayerViewSet, basename='game-players')

urlpatterns = router.urls + games_router.urls
