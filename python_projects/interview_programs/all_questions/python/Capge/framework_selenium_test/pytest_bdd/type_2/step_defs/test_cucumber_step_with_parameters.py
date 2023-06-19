# update 2

from pytest_bdd import *
from pytest_bdd import parsers
import pytest

# for global variable
def pytest_configure():
    pytest.total= 0
    print("\n\nInitially: ", pytest.total)



@scenario(r'..\features\cucumbers_with_parameters.feature', 'Add Cucumbers in my basket parameters')
def test_add_cucumbers_in_my_basket():
    print("This will be executed at the end of test")

@scenario(r'..\features\cucumbers_with_parameters.feature', 'Remove Cucumbers from my basket parameters')
def test_remove_cucumbers_from_my_basket():
    print("This will be executed at the end of test")
    

# I have not used fixture here

@given(parsers.cfparse(r'The basket has "{initial:Number}" cucumbers parameters', extra_types= {"Number": int})) # Number is imp else bydefault it will str
def basket(initial):
    pytest.total= initial
    print("Initail is:", pytest.total)

@when(parsers.cfparse('"{some:Number}" Cucumbers are added to the basket parameters', extra_types= {"Number": int}))
def add_cucumbers(some):
    pytest.total= pytest.total + some
    print("After adding: ", some)

@when(parsers.cfparse('"{some:Number}" Cucumbers are removed from the basket parameters', extra_types= {"Number": int}))
def remove_cucumbers(some):
    pytest.total= pytest.total - some
    print("After Removing: ", some)

@then(parsers.cfparse('the basket conatins "{total:Number}" cucumbers parameters' , extra_types= {"Number": int}))
def basket_has_total(total):
    print("Total is: ", pytest.total)
    assert pytest.total == total