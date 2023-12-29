import factory
from factory.django import DjangoModelFactory

from store.models import Category,Product,Price,ProductImage,ProductSizes



class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.Sequence(lambda n: "Category_%d" % n )
    
class PriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Price
        
    product = factory.SubFactory('tests.factories.ProductFactory')   
    price = factory.Faker('pydecimal', left_digits=4, right_digits=2)
    quantity = factory.Faker('random_int', min=1, max=100)
    
class ProductImageFactory(DjangoModelFactory):
    class Meta:
        model = ProductImage

    product = factory.SubFactory('tests.factories.ProductFactory')
    
    image = factory.django.ImageField()

    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = factory.Sequence(lambda n: "product_%d" % n )
    status = Product.PENDING
    category = factory.RelatedFactoryList(CategoryFactory, size=2)
    # price = factory.RelatedFactoryList(PriceFactory)
    # product_image = factory.SubFactory(ProductImageFactory)
    
class SizeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSizes
    size = factory.Sequence(lambda n: "size_%d" % n )
                

    

 