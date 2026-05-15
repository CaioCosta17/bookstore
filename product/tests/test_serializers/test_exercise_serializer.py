import pytest
from product.factories import ProductFactory
from product.serializers.product_exercise_serializers import ProductSerializer

@pytest.mark.django_db
def test_exercise_product_serializer():
    product = ProductFactory.build()
    serializer = ProductSerializer(product)
    
    # Verifica se os dados serializados batem com o que foi criado
    assert serializer.data['title'] == product.title
    assert float(serializer.data['price']) == float(product.price)