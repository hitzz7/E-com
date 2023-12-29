
import pytest
from django.test import RequestFactory
from store.models import Category,Price,Product,ProductSizes
from store.serializers import CategorySerializer,PriceSerializer,ProductSerializer,ProductImageSerializer
from django.test import TestCase
pytestmark = pytest.mark.django_db

class TestCategorySerializer:
    
    def test_category_serializer_to_representation(self):
        # Create a Category instance without soft-deleting
        category_not_deleted = Category.objects.create(name='Category 1', is_deleted=False)

        # Create a Category instance with soft-deleting
        category_soft_deleted = Category.objects.create(name='Category 2', is_deleted=True)

        # Create a CategorySerializer for each instance
        serializer_not_deleted = CategorySerializer(instance=category_not_deleted)
        serializer_soft_deleted = CategorySerializer(instance=category_soft_deleted)

        # Check representation for not deleted category
        representation_not_deleted = serializer_not_deleted.data
        assert representation_not_deleted['id'] == category_not_deleted.id
        assert representation_not_deleted['name'] == category_not_deleted.name
        assert representation_not_deleted['is_deleted'] == category_not_deleted.is_deleted

        # Check representation for soft deleted category
        # representation_soft_deleted = serializer_soft_deleted.data
        # assert representation_soft_deleted['id'] == 404

        # Clean up
        category_not_deleted.delete()
        category_soft_deleted.delete()

   

class TestPriceSerializer():
    def test_serializer_output(self):
        # Create a Product instance for testing
        product_instance = Product(name="Test Product")
        product_instance.save()

        # Create a Price instance associated with the Product
        price_instance = Price(product=product_instance, quantity=10, price=25.99)
        price_instance.save()

        # Serialize the Price instance using the serializer
        serializer = PriceSerializer(price_instance)
        serialized_data = serializer.data

        # Check if the expected fields are present
        assert 'id' in serialized_data
        assert 'quantity' in serialized_data
        assert 'price' in serialized_data
        assert 'f_price' in serialized_data

        # Check the format of f_price
        assert serialized_data['f_price'] == '$25.99'
        
    
        
class TestProductSerializer(TestCase):
    def test_serializer_create(self):
        # Create Category and ProductSizes instances for testing
        category1 = Category.objects.create(name='Category 1')
        category2 = Category.objects.create(name='Category 2')
        

        # Prepare data for creating a Product instance
        product_data = {
            'name': 'Test Product',
            
            'category': [category1.id, category2.id],
            
            'prices': [{'quantity': 10, 'price': 25.99}, {'quantity': 20, 'price': 49.99}],
            
        }

        # Serialize and create the Product instance
        serializer = ProductSerializer(data=product_data)
        serializer.is_valid(raise_exception=True)
        product_instance = serializer.save()

        # Check if the Product instance was created correctly
        assert Product.objects.count() == 1
        assert product_instance.name == 'Test Product'
        
        assert product_instance.category.count() == 2
        
        assert product_instance.prices.count() == 2
        
    def test_product_repereenation(self):
        product_not_deleted = Product.objects.create(name="product1",is_deleted=False)
        product_soft_deleted = Product.objects.create(name="product2",is_deleted=True)
        serializer_not_deleted = ProductSerializer(instance=product_not_deleted)
        serializer_soft_deleted = ProductSerializer(instance=product_soft_deleted)
        
        representation_not_deleted = serializer_not_deleted.data
        assert representation_not_deleted['id'] == product_not_deleted.id
        
       

class TestProductImageSerializer:
    
        
    def test_get_thumbnail(self, product_image_factory,product_factory):
        your_product_instance= product_factory()
        product_image = product_image_factory(image='example.jpg', product=your_product_instance)
        serializer = ProductImageSerializer(instance=product_image)
        thumbnail_url = serializer.get_thumbnail(product_image)

        # Perform assertions based on your expectations
        assert 'example.jpg' in thumbnail_url
        # Add more assertions if needed

    def test_get_thumbnail400(self, product_image_factory,product_factory):
        your_product_instance= product_factory()
        product_image = product_image_factory(image='example.jpg', product=your_product_instance)
        serializer = ProductImageSerializer(instance=product_image)
        thumbnail400_url = serializer.get_thumbnail400(product_image)

        # Perform assertions based on your expectations
        assert 'example.jpg' in thumbnail400_url
        # Add more assertions if needed

    def test_get_thumbnail1200(self, product_image_factory,product_factory):
        your_product_instance= product_factory()
        product_image = product_image_factory(image='example.jpg', product=your_product_instance)
        serializer = ProductImageSerializer(instance=product_image)
        thumbnail1200_url = serializer.get_thumbnail1200(product_image)

        # Perform assertions based on your expectations
        assert 'example.jpg' in thumbnail1200_url