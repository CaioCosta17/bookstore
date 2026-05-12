from rest_framework import serializers
from order.models import Order

class OrderExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'