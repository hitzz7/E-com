from django.db import models
from django.core.files.base import ContentFile
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
from io import BytesIO  
import os
from django.conf import settings
from datetime import datetime
import uuid
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=255,unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
        
    def retrive(self):
        self.is_deleted = False
        self.save()
    
    class MPTTMeta:
        order_insertion_by =["name"]
        
    class Meta:
        indexes = [
            
            models.Index(fields=["is_deleted"]),
            
        ]
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    
    name = models.CharField(max_length=255)
    PENDING='pending'
    ACTIVE='active'
    Inactive='inactive'
    status_choices=(
        (PENDING,'pending'),
        (ACTIVE,'active'),
        (Inactive,'inactive'),
        
        
    )
    
        

    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=PENDING,
    )

    category = models.ManyToManyField("Category",blank=True)
    sizes = models.ManyToManyField("ProductSizes")
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
        
    def retrive(self):
        self.is_deleted = False
        self.save()
    
    class Meta:
        indexes = [
            models.Index(fields=["name","is_deleted",'status']),
            
            
            
        ]
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(upload_to ='',blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
    class Meta:
        indexes = [
            models.Index(fields=["image","is_deleted"]),
            
            
        ]
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
    def retrive(self):
        self.is_deleted = False
        self.save()
    
    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        
        if self.image:
            
            thumbnail_data = self.get_thumbnail()

           
            thumbnail_folder = os.path.join(settings.MEDIA_ROOT, 'thumbnails')

            
            os.makedirs(thumbnail_folder, exist_ok=True)
            original_image_name = os.path.basename(self.image.name)

            
            thumbnail_name = 'thumbnail'+ original_image_name

            
            thumbnail_path = os.path.join(thumbnail_folder, thumbnail_name)

            
            with open(thumbnail_path, 'wb') as thumbnail_file:
                thumbnail_file.write(thumbnail_data.read())
                
        if self.image:
            
            thumbnail_data = self.get_thumbnail400()

            
            thumbnail_folder = os.path.join(settings.MEDIA_ROOT, 'thumbnail400')

            
            os.makedirs(thumbnail_folder, exist_ok=True)
            original_image_name = os.path.basename(self.image.name)

            
            thumbnail_name = 'thumbnail'+ original_image_name

            
            thumbnail_path = os.path.join(thumbnail_folder, thumbnail_name)

            
            with open(thumbnail_path, 'wb') as thumbnail_file:
                thumbnail_file.write(thumbnail_data.read())
                
        if self.image:
            
            thumbnail_data = self.get_thumbnail1200()

            
            thumbnail_folder = os.path.join(settings.MEDIA_ROOT, 'thumbnail1200')

            
            os.makedirs(thumbnail_folder, exist_ok=True)
            original_image_name = os.path.basename(self.image.name)

           
            thumbnail_name = 'thumbnail'+ original_image_name

            
            thumbnail_path = os.path.join(thumbnail_folder, thumbnail_name)

            
            with open(thumbnail_path, 'wb') as thumbnail_file:
                thumbnail_file.write(thumbnail_data.read())
    
    
    def get_thumbnail(self):
        image_path = self.image.path
        img = Image.open(image_path)
        img.thumbnail((100, 100))
        thumbnail_buffer = BytesIO()
        img.save(thumbnail_buffer, format='PNG')
        
        thumbnail_data = thumbnail_buffer.getvalue()
        
        img.close()
        thumbnail_buffer.close()
        
        return BytesIO(thumbnail_data)
    
    
        #
        
    def get_thumbnail400(self):
        image_path = self.image.path
        img = Image.open(image_path)
        img.thumbnail((400, 400))
        thumbnail_buffer = BytesIO()
        img.save(thumbnail_buffer, format='PNG')
        thumbnail_data = thumbnail_buffer.getvalue()
        
        img.close()
        thumbnail_buffer.close()
        return BytesIO(thumbnail_data)
    
    def get_thumbnail1200(self):
        image_path = self.image.path
        img = Image.open(image_path)
        img.thumbnail((1200, 1200))
        thumbnail_buffer = BytesIO()
        img.save(thumbnail_buffer, format='PNG')
        thumbnail_data = thumbnail_buffer.getvalue()
        
        img.close()
        thumbnail_buffer.close()
        return BytesIO(thumbnail_data)
    
    def get_thumbnail_url(self, size):
        thumbnail_folder = 'thumbnails' if size == (100, 100) else 'thumbnail400' if size == (400, 400) else 'thumbnail1200'
        thumbnail_name = f'thumbnail{os.path.basename(self.image.name)}'
        thumbnail_path = os.path.join( thumbnail_folder, thumbnail_name)
        return f"{settings.MEDIA_URL}{thumbnail_path.replace(os.path.sep, '/')}"
    
    
   
    
        
class Price(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="prices")
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.IntegerField(default=100)
    is_deleted = models.BooleanField(default=False)
    
    def f_price(self):
        return "${:.2f}".format(self.price)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
    def retrive(self):
        self.is_deleted = False
        self.save()
    
    
    def __str__(self):

        return f"Price:{self.price} for {self.product.name}"
    
    class Meta:
        indexes = [
            models.Index(fields=["price","quantity","is_deleted"]),
            models.Index(fields=["product_id"]),
            
            
        ]
    


    
class ProductSizes(models.Model):
    
    size = models.CharField(max_length=5)
    is_deleted = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.is_deleted = True
        self.save()
    
    def retrive(self):
        self.is_deleted = False
        self.save()
    
    
    class MPTTMeta:
        order_insertion_by =["size"]
        
    class Meta:
        indexes = [
            models.Index(fields=["size","is_deleted"]),
            
            
        ]
    
    def __str__(self):
        return self.size




        

        
        
        