from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.viewsets.simple_viewsets import SimpleCategoryViewSet, SimpleOrderViewSet, SimpleProductViewSet

router = DefaultRouter()

router.register(r'simple-categories', SimpleCategoryViewSet, basename='simple-category')
router.register(r'simple-products', SimpleProductViewSet, basename='simple-product')
router.register(r'simple-orders', SimpleOrderViewSet, basename='simple-order')

urlpatterns = [
    path('simple-api/', include(router.urls)),
]