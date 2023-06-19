from pytest_bdd import *
from pathlib import Path  # To get feature file
import pytest

feature_file_dir= "features"
feature_file= "withdraw_amount.feature"
BASE_DIR= Path(__file__).resolve().parent
FEATURE_FILE= BASE_DIR.joinpath(feature_file_dir).joinpath(feature_file)


# for global variable
def pytest_configure():
    pytest.AMT= 0


@scenario(FEATURE_FILE, "Withdrawl of money")
def test_withdrawl():
    print("Withdrwal is done")

@given("The account balance is 100EUR")
def current_balance():
    pytest.AMT= 100
    print("current_balance: ", pytest.AMT)

@when("The account holder withdraws 30EUR")
def amt_withdrwan():
    withdrawl= 30
    pytest.AMT= 100 - withdrawl
    print("after withdrawl, current_balance: ", pytest.AMT)

@then("The account balance should be 70EUR")
def amount_left_verify():
    print("current_balance: ", pytest.AMT)
    assert pytest.AMT == 70

