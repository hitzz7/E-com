from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Category,Product,ProductImage,Price,ProductSizes
from .serializers import CategorySerializer,ProductSerializer,ProductImageSerializer,PriceSerializer,ProductSizeSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class =CategorySerializer
    
    
    def get_queryset(self):
        
            
            return Category.objects.filter(is_deleted=False)
    

        
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, pk=kwargs['pk'])
        instance.delete()
        
        return Response({'status': 'hard deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='soft-delete')
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'status': 'soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='retrive')
    def retrive(self, request, *args, **kwargs):
        instance = get_object_or_404(Category, pk=kwargs['pk'])
        instance.is_deleted = False
        instance.save()
        return Response({'status': 'retrived'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset=ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
    def get_queryset(self):
        
        return ProductImage.objects.filter(is_deleted=False)
    
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(ProductImage, pk=kwargs['pk'])
        instance.delete()
        
        return Response({'status': 'hard deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='soft-delete')
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'status': 'soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    @action(detail=True, methods=['DELETE'], url_path='retrive')
    def retrive(self, request, *args, **kwargs):
        instance = get_object_or_404(ProductImage, pk=kwargs['pk'])
        instance.is_deleted = False
        instance.save()
        return Response({'status': 'retrived'}, status=status.HTTP_204_NO_CONTENT)
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        
        return Product.objects.filter(is_deleted=False)
    
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Product, pk=kwargs['pk'])
        instance.delete()
        
        return Response({'status': 'hard deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='soft-delete')
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'status': 'soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='retrive')
    def retrive(self, request, *args, **kwargs):
        instance = get_object_or_404(Product, pk=kwargs['pk'])
        instance.is_deleted = False
        instance.save()
        return Response({'status': 'retrived'}, status=status.HTTP_204_NO_CONTENT)
    
class PriceViewSet(viewsets.ModelViewSet):
    queryset=Price.objects.all()
    serializer_class = PriceSerializer
    
    def get_queryset(self):
        
        return Price.objects.filter(is_deleted=False)
    
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Price, pk=kwargs['pk'])
        instance.delete()
        
        return Response({'status': 'hard deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='soft-delete')
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'status': 'soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='retrive')
    def retrive(self, request, *args, **kwargs):
        instance = get_object_or_404(Price, pk=kwargs['pk'])
        instance.is_deleted = False
        instance.save()
        return Response({'status': 'retrived'}, status=status.HTTP_204_NO_CONTENT)
    
class ProductSizeViewSet(viewsets.ModelViewSet):
    queryset=ProductSizes.objects.all()
    serializer_class = ProductSizeSerializer
    
    def get_queryset(self):
        
        return ProductSizes.objects.filter(is_deleted=False)
    
    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(ProductSizes, pk=kwargs['pk'])
        instance.delete()
        
        return Response({'status': 'hard deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='soft-delete')
    def soft_delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response({'status': 'soft deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['DELETE'], url_path='retrive')
    def retrive(self, request, *args, **kwargs):
        instance = get_object_or_404(ProductSizes, pk=kwargs['pk'])
        instance.is_deleted = False
        instance.save()
        return Response({'status': 'retrived'}, status=status.HTTP_204_NO_CONTENT)
    