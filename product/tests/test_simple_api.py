import pytest
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
class TestSimpleAPIEndpoints:
    
    def setup_method(self):
        self.client = APIClient()

    def test_category_crud_operations(self):
        category_payload = {
            "title": "Smartphones"
        }
        
        post_response = self.client.post(
            '/simple-api/simple-categories/', 
            data=category_payload, 
            format='json'
        )
        assert post_response.status_code == status.HTTP_201_CREATED, f"Failed: {post_response.data}"

        get_response = self.client.get('/simple-api/simple-categories/')
        assert get_response.status_code == status.HTTP_200_OK
        assert len(get_response.data) > 0

    def test_product_list_endpoint(self):
        response = self.client.get('/simple-api/simple-products/')
        assert response.status_code == status.HTTP_200_OK

    def test_order_list_endpoint(self):
        response = self.client.get('/simple-api/simple-orders/')
        assert response.status_code == status.HTTP_200_OK