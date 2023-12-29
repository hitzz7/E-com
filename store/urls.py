from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,ProductImageViewSet,ProductViewSet,PriceViewSet,ProductSizeViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'image', ProductImageViewSet, basename='image')
router.register(r'price', PriceViewSet, basename='price')
router.register(r'size', ProductSizeViewSet, basename='size')
urlpatterns = router.urls