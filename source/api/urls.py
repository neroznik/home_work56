from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import get_token_view, ProductViewSet, UserViewSet, OrderViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('', include(router.urls)),
]
