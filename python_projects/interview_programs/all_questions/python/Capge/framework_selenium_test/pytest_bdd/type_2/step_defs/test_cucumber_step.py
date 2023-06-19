# update 1

from pytest_bdd import *
from utilities_python.Capge.framework_selenium_test.pytest_bdd.type_2.cucumbers_add_remove import CucumberBasket
import pytest

@scenario(r'..\features\cucumbers.feature', 'Add Cucumbers in my basket')
def test_add_cucumbers_in_my_basket():
    """Add Cucumbers in my basket."""
    print("This will be executed at the end of test")

@pytest.fixture()  # We are using fixtures here
def basket():
    """The basket has 2 cucumbers."""
    value = CucumberBasket(initial_count= 2)
    return value


@when('4 Cucumbers are added to the basket')
def add_cucumbers(basket):
    """4 Cucumbers are added to the basket."""
    basket.add(4)


@then('the basket conatins 6 cucumbers')
def basket_has_total(basket):
    """the basket conatins 6 cucumbers."""
    assert basket.count == 6