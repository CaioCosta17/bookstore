from rest_framework import viewsets
from product.models import Category, Product, Order
from product.serializers import CategorySerializer, ProductSerializer, OrderSerializer

class SimpleCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SimpleProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SimpleOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer