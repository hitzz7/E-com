
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Category

# class CategoryAPITest(APITestCase):
    
#     def test_create_category(self):
#         # Test creating a new category
#         data = {'name': 'Test Category'}
#         response = self.client.post(self.url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Category.objects.count(), 1)
#         self.assertEqual(Category.objects.get().name, 'Test Category')
