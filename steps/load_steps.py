from behave import given
from tests.factories import ProductFactory

@given('there are products in the database')
def step_impl(context):
    ProductFactory.create_batch(5)
