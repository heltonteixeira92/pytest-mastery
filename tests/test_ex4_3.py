import pytest

from django.contrib.auth.models import User


def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert True
