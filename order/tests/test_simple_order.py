import pytest
from rest_framework.test import APIClient
from rest_framework import status
from product.models import Category, Product

@pytest.mark.django_db
class TestSimpleOrderAPI:
    
    def setup_method(self):
        self.client = APIClient()
        
        self.category = Category.objects.create(
            title="Gaming", 
            slug="gaming", 
            active=True
        )
        self.product = Product.objects.create(
            title="Video Game Console", 
            price=500.00,
            active=True
        )
        self.product.category.add(self.category)

    def test_create_order(self):
        payload = {
            "product": [self.product.id]
        }
        
        response = self.client.post(
            '/simple-api/simple-orders/', 
            data=payload, 
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_orders(self):
        response = self.client.get('/simple-api/simple-orders/')
        
        assert response.status_code == status.HTTP_200_OK