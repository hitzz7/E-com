from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import CategoryFactory,ProductFactory,PriceFactory,ProductImageFactory,SizeFactory
import pytest
register(CategoryFactory)
register(ProductFactory)
register(SizeFactory)
register(PriceFactory)
register(ProductImageFactory)

@pytest.fixture
def api_client():
    return APIClient