import pytest
from rest_framework.test import APIClient
from rest_framework import status
from product.models import Category

@pytest.mark.django_db
class TestSimpleCategoryAPI:
    
    def setup_method(self):
        self.client = APIClient()

    def test_create_category(self):
        payload = {
            "title": "Electronics",
            "slug": "electronics",
            "active": True
        }
        
        response = self.client.post(
            '/simple-api/simple-categories/', 
            data=payload, 
            format='json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_categories(self):
        Category.objects.create(title="Books", slug="books", active=True)
        
        response = self.client.get('/simple-api/simple-categories/')
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0