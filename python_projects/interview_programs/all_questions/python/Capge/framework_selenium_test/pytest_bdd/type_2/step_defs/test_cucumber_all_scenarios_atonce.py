# update 3 . Its  Best practice

from pytest_bdd import scenarios, parsers, given, when, then

from utilities_python.Capge.framework_selenium_test.pytest_bdd.type_2.cucumbers_add_remove import CucumberBasket

EXTRA_TYPES = {
    'Number': int,
}

scenarios('../features/cucumbers_with_parameters.feature')

# Fixture is used
@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers parameters', extra_types=EXTRA_TYPES),
       target_fixture='basket')
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket parameters', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket parameters', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket conatins "{total:Number}" cucumbers parameters', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total
