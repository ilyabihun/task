from django.urls import path, include

from rest_framework.routers import SimpleRouter

from main.views import MessageViewSet, TicketViewSet, UserViewSet

router = SimpleRouter()
router.register('messages', MessageViewSet, basename='messages')
router.register('tickets', TicketViewSet, basename='tickets')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls',
                 namespace='rest_framework')),
]
