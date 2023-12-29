import pytest
import json
import os
from django.core.files.uploadedfile import SimpleUploadedFile
import io
pytestmark = pytest.mark.django_db

class TestCategoryEndPoints:
    
    endpoint="/api/category/"
    
    def test_category_get(self,category_factory,api_client):
        category_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200 
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 4
        
    def test_category_getdetail(self,category_factory,api_client):
        category = category_factory()
        response = api_client().get(f"{self.endpoint}{category.id}/")
        assert response.status_code == 200 
       
        category_data = response.json()
        assert category_data["id"] == category.id
        assert category_data["name"] == category.name
        
    def test_category_post(self, category_factory, api_client):
        new_category_data ={"name":"new category"}
        response = api_client().post(self.endpoint, data=new_category_data)
        assert response.status_code == 201
        new_category = json.loads(response.content)
        print(json.loads(response.content))
        assert new_category["name"] == "new category"
        
        
    def test_category_update(self, category_factory, api_client):
        category = category_factory()
        updated_category_data = {"name": "Updated Category"}
        response = api_client().put(f"{self.endpoint}{category.id}/", data=updated_category_data)
        assert response.status_code == 200
        updated_category = json.loads(response.content)
        print(json.loads(response.content))
        assert updated_category["name"] == "Updated Category"
        
    def test_category_delete(self, category_factory, api_client):
        category = category_factory()
        response = api_client().delete(f"{self.endpoint}{category.id}/")
        assert response.status_code == 204
        
    
        
        
    
        
class TestProductEndPoints:
    endpoint="/api/product/"
    
    def test_product_get(self,product_factory,api_client):
        product_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200 
       
    def test_product_post(self, api_client,category_factory,price_factory):
        
        category1 = category_factory()
        category2 = category_factory()
        
        
        
        
        
        new_product_data ={"name":"new product","category": [category1.id, category2.id],}
        response = api_client().post(self.endpoint, data=new_product_data)
        assert response.status_code == 201
        new_product = json.loads(response.content)
        print(json.loads(response.content))
        assert new_product["name"] == "new product"
        
        
    def test_product_update(self, product_factory, api_client,category_factory):
        product = product_factory()
        category1 = category_factory()
        category2 = category_factory()
        
        updated_product_data = {"name": "Updated Product","category": [category1.id, category2.id]}
        response = api_client().put(f"{self.endpoint}{product.id}/", data=updated_product_data)
        assert response.status_code == 200
        updated_product = json.loads(response.content)
        print(json.loads(response.content))
        assert updated_product["name"] == "Updated Product"
        
    def test_product_delete(self, product_factory, api_client):
        product = product_factory()
        response = api_client().delete(f"{self.endpoint}{product.id}/")
        assert response.status_code == 204
        
    
    
   
class TestImageEndPoints:
    
    endpoint="/api/image/"
    
    def test_image_get(self,product_image_factory,api_client):
        product_image_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200 
        print(json.loads(response.content))
        
    