# update 5 , parameterizing in step def in not recommended. Also now, its not working

# VVI->  This is not recommeneded way, use scenario outline with examples is more convenient.
# and people expect example, if you write scenario outline in Gherkin feature file

from pytest_bdd import scenario, parsers, given, when, then
from utilities_python.Capge.framework_selenium_test.pytest_bdd.type_2.cucumbers_add_remove import CucumberBasket
import pytest

EXTRA_TYPES = {
    'Number': int
}

@pytest.mark.parametrize(
    ["initial", "some", "total"], [(2, 4, 6), (0, 3, 10), (1, 2, 3), (5, 4, 9)
                                   ])
@scenario(r'..\features\cucumbers_similar_scenario_outlines_without_example.feature',
          'Add Cucumbers in my basket parameters')
def test_add_cucumbers_in_my_basket(initial, some, total):
    """Add Cucumbers in my basket."""
    print("This will be executed at the end of test")


@pytest.mark.parametrize(
    ["initial", "some", "total"], [(2, 4, 6), (0, 3, 10), (1, 2, 3), (5, 4, 9)
                                   ])
@scenario(r'..\features\cucumbers_similar_scenario_outlines_without_example.feature',
          'Remove Cucumbers from my basket parameters')
def test_remove_cucumbers_from_my_basket(initial, some, total):
    print("This will be executed at the end of test")

# Fixture is used
@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers parameters', extra_types=EXTRA_TYPES),
       target_fixture='basket')
@given('the basket has "<initial>" cucumbers', target_fixture='basket')
def basket(initial):
    print("Initial: ", initial)
    return CucumberBasket(initial_count= initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket parameters', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are added to the basket')
def add_cucumbers(basket, some):
    print("Some is: ", some)
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket parameters', extra_types=EXTRA_TYPES))
@when('"<some>" cucumbers are removed from the basket')
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket conatins "{total:Number}" cucumbers parameters', extra_types=EXTRA_TYPES))
@then('the basket contains "<total>" cucumbers')
def basket_has_total(basket, total):
    assert basket.count == total
