Feature: Bank Transaction
  Tests pertaining to banking transaction like withdrawl and deposit

  Scenario: Withdrawl of money
    Given The account balance is 100EUR
    When The account holder withdraws 30EUR
    Then The account balance should be 70EUR