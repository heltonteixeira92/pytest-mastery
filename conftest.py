"""
this file can be utilized to set up our fixtures
pytest will look to this file before it runs any tests

Introducing Factory Boy and Faker - Fixture Replacement
"""
import pytest

from django.contrib.auth.models import User


from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user
