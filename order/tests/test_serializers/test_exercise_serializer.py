import pytest
from order.factories import OrderFactory
from order.serializers.order_exercise_serializers import OrderExerciseSerializer

@pytest.mark.django_db
def test_exercise_order_serializer():
    order = OrderFactory.build()
    
    serializer = OrderExerciseSerializer(order)
    
    assert 'id' in serializer.data