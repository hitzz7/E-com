import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from store.models import Category

pytestmark = pytest.mark.django_db

class TestCategoryviews:
    endpoint="/api/category/"
    
    def category(self, category_factory):
        return category_factory(is_deleted=False)
        
    
    def test_soft_delete_category(self,api_client, category_factory):
        # Create a category using the factory
        category = category_factory()
    
    # Define the URL for the detail view
    
    
    # Send a DELETE request to the URL
        response = api_client().delete(f"{self.endpoint}{category.id}/soft-delete/")
    
    # Check that the response status code is 204 (No Content)
        assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Refresh the category from the database to get the updated value
        category.refresh_from_db()
    
    # Assert that the category is soft deleted
        assert category.is_deleted is True
        
class TestProductviews:
    endpoint="/api/product/"
    
    def product(self, product_factory):
        return product_factory(is_deleted=False)
        
    
    def test_soft_delete_product(self,api_client, product_factory):
        # Create a category using the factory
        product = product_factory()
    
    # Define the URL for the detail view
    
    
    # Send a DELETE request to the URL
        response = api_client().delete(f"{self.endpoint}{product.id}/soft-delete/")
    
    # Check that the response status code is 204 (No Content)
        assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Refresh the category from the database to get the updated value
        product.refresh_from_db()
    
    # Assert that the category is soft deleted
        assert product.is_deleted is True

class TestProducImageviews:
    endpoint="/api/image/"
    
    def productimage(self, product_image_factory):
        return product_image_factory(is_deleted=False)
        
    
    def test_soft_delete_image(self,api_client,product_image_factory):
        # Create a category using the factory
        productimage = product_image_factory()
    
    # Define the URL for the detail view
    
    
    # Send a DELETE request to the URL
        response = api_client().delete(f"{self.endpoint}{productimage.id}/soft-delete/")
    
    # Check that the response status code is 204 (No Content)
        assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Refresh the category from the database to get the updated value
        productimage.refresh_from_db()
    
    # Assert that the category is soft deleted
        assert productimage.is_deleted is True
        
class TestPriceviews:
    endpoint="/api/price/"
    
    def price(self, price_factory):
        return price_factory(is_deleted=False)
        
    
    def test_soft_delete_price(self,api_client, price_factory):
        # Create a category using the factory
        price = price_factory()
    
    # Define the URL for the detail view
    
    
    # Send a DELETE request to the URL
        response = api_client().delete(f"{self.endpoint}{price.id}/soft-delete/")
    
    # Check that the response status code is 204 (No Content)
        assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Refresh the category from the database to get the updated value
        price.refresh_from_db()
    
    # Assert that the category is soft deleted
        assert price.is_deleted is True
        

    
        

        
