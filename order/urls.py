from django.urls import path, include
from rest_framework import routers

from .viewsets import order_viewset

router = routers.SimpleRouter()
router.register(r'order', order_viewset.OrderViewSet, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]