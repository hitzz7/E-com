from rest_framework import serializers
from .models import Category, Product,ProductImage,Price,ProductSizes


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','name','is_deleted']
    
        
    def to_representation(self, instance):
        if instance.is_deleted:
            return None  # Exclude soft-deleted images from the serialization
        return super().to_representation(instance)


    
        
class ProductImageSerializer(serializers.ModelSerializer):
    
    thumbnail = serializers.SerializerMethodField()
    thumbnail400 = serializers.SerializerMethodField()
    thumbnail1200 = serializers.SerializerMethodField()
    class Meta:
        model = ProductImage
        fields = ['id','image','thumbnail','thumbnail400','thumbnail1200','product']
        
    
    def to_representation(self, instance):
        if instance.is_deleted:
            return None  # Exclude soft-deleted images from the serialization
        return super().to_representation(instance)

        
    def get_thumbnail(self, instance):
        return instance.get_thumbnail_url((100, 100))

    def get_thumbnail400(self, instance):
        return instance.get_thumbnail_url((400, 400))

    def get_thumbnail1200(self, instance):
        return instance.get_thumbnail_url((1200, 1200))
        
class PriceSerializer(serializers.ModelSerializer):
    f_price = serializers.SerializerMethodField()
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Price
        fields = ['id','quantity','price','f_price',]
        
   
        
    def to_representation(self, instance):
        # Exclude soft-deleted products
        if instance.is_deleted:
            return None
        return super().to_representation(instance)
        
    def get_f_price(self, obj):
            return "${:.2f}".format(obj.price)
        
        

class ProductSizeSerializer(serializers.ModelSerializer):
    
    
    
    
    class Meta:
        model = ProductSizes
        fields = '__all__'
        
   
        
    def to_representation(self, instance):
        if instance.is_deleted:
            return None  # Exclude soft-deleted images from the serialization
        return super().to_representation(instance)
   
   
        
        




class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.filter(is_deleted=False), many=True)
    images = ProductImageSerializer(many=True,required=False)
    prices = PriceSerializer(many=True,required=False)
    sizes = serializers.SlugRelatedField(queryset=ProductSizes.objects.filter(is_deleted=False),many=True,slug_field='size',required=False)
   
    class Meta:
        model = Product
        fields = '__all__'
        
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'prices' in representation:
            representation['prices'] = Price.objects.filter(product=instance, is_deleted=False).values()
            
        if 'category' in representation:
             representation['category'] = instance.category.filter(is_deleted=False).values_list('id', flat=True)
             
        if 'sizes' in representation:
            
             representation['sizes'] = instance.sizes.filter(is_deleted=False).values_list('size', flat=True)

        return representation
        
   
        
    def create(self, validated_data):
        categoryes_data = validated_data.pop('category',[])
        sizes_data = validated_data.pop('sizes',[])
        prices_data = validated_data.pop('prices',[])
        
        
        product_instance = Product.objects.create(**validated_data)
        product_instance.category.set(categoryes_data)
        product_instance.sizes.set(sizes_data)
        
            
            
        for price_data in prices_data:
            Price.objects.create(product=product_instance,**price_data)
        
       
        
        
        
        return product_instance
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category.set(validated_data.get('category', instance.category.all()))
        instance.sizes.set(validated_data.get('sizes', instance.sizes.all()))

        prices_data = validated_data.get('prices', [])
        for price_data in prices_data:
            price_id = price_data.get('id', None)
            if price_id:
               
                price_instance = Price.objects.get(id=price_id, product=instance)
                price_instance.price = price_data.get('price', price_instance.price)
                price_instance.quantity = price_data.get('quantity', price_instance.quantity)
                price_instance.save()
            else:
                
                Price.objects.create(product=instance, **price_data)

        return instance
    
   
            
        
    

