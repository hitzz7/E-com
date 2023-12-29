import os
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from PIL import Image
from io import BytesIO
import pytest

pytestmark = pytest.mark.django_db




class TestCategoryModel:
    def test_str_method(self,category_factory):
        obj = category_factory(name="category")
        assert obj.__str__() =="category"
        
    def test_softdelete(self,category_factory):
        obj =  category_factory()
        obj.soft_delete()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is True
        
    def test_retrive(self,category_factory):
        obj =  category_factory()
        obj.retrive()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is False


class TestProductModel:
    def test_str_method(self,product_factory):
        obj = product_factory(name="test_product")
        assert obj.__str__() =="test_product"
        
    def test_softdelete(self,product_factory):
        obj =  product_factory()
        obj.soft_delete()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is True
        
    def test_retrive(self,product_factory):
        obj =  product_factory()
        obj.retrive()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is False
        
   



class TestProductImageModel:
    def test_product_image_creation(self,product_image_factory):
        product_image = product_image_factory()
        assert product_image.product is not None
        assert str(product_image) == f"Image for {product_image.product.name}"
        
    def test_product_image_get_thumbnail(self, product_image_factory):
        product_image = product_image_factory()
        thumbnail_data = product_image.get_thumbnail()

        thumbnail_image = Image.open(BytesIO(thumbnail_data.getvalue()))
        assert thumbnail_image.width == 100
        assert thumbnail_image.height == 100
        assert thumbnail_image.format == 'PNG'

        thumbnail_image.close()
        thumbnail_data.close()
        
    def test_softdelete(self,product_image_factory):
        obj =  product_image_factory()
        obj.soft_delete()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is True
    def test_retrive(self,product_image_factory):
        obj =  product_image_factory()
        obj.retrive()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is False

        
        
    def test_product_image_save_thumbnails(self,product_image_factory):
       
        product_image = product_image_factory()

        
        product_image.save()

        
        assert product_image.get_thumbnail_url((100, 100)) == f"{settings.MEDIA_URL}thumbnails/thumbnail{os.path.basename(product_image.image.name)}"
        assert product_image.get_thumbnail_url((400, 400)) == f"{settings.MEDIA_URL}thumbnail400/thumbnail{os.path.basename(product_image.image.name)}"
        assert product_image.get_thumbnail_url((1200, 1200)) == f"{settings.MEDIA_URL}thumbnail1200/thumbnail{os.path.basename(product_image.image.name)}"

    


class TestPriceModel:
    def test_price_str_method(self,price_factory,product_factory):
        product = product_factory(name="Test Product")
        price = price_factory(product=product, price=25.99, quantity=10)
        
        assert str(price) == f"Price:25.99 for {product.name}"
    
    def test_softdelete(self,price_factory):
        obj =  price_factory()
        obj.soft_delete()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is True
        
    def test_retrive(self,price_factory):
        obj =  price_factory()
        obj.retrive()
        
        obj.refresh_from_db()
        
        assert obj.is_deleted is False
        
    
class TestSizeModel:
    def test_str_size(self,size_factory):
        obj = size_factory(size="S")
        assert obj.__str__() == "S"
        
        