from rest_framework import serializers

from product.models import Product, product
from product.serializers.product_serializers import ProductSerializers

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializers(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for porduct in instance.product.all()])
        return total
    
    class Meta: 
        model = Product
        fields = ['product', 'total']