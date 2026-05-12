from rest_framework import serializers
from product.models import Product
from order.models import Order
from product.serializers.product_serializers import ProductSerializers

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializers(required=True, many=True)
    total = serializers.SerializerMethodField()
    
    def get_total(self, instance):
        total = sum([p.price for p in instance.product.all()])
        return total
        
    class Meta:
        model = Order
        fields = ['product', 'total']