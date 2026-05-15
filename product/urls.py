from django.urls import path, include
from rest_framework import routers

from product.viewsets.product_viewset import ProductViewSet

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'category', ProductViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('product.simple_urls'))
]