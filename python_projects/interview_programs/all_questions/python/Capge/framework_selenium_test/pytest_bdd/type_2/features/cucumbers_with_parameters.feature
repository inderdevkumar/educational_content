Feature: Cucumber Basket
  This will be a comment
  As a gardener,
  I like to carry cucmbetrs in my basket.

  Scenario: Add Cucumbers in my basket parameters
    Given The basket has "2" cucumbers parameters
    When "4" Cucumbers are added to the basket parameters
    Then the basket conatins "6" cucumbers parameters


  Scenario: Remove Cucumbers from my basket parameters
    Given The basket has "10" cucumbers parameters
    When "4" Cucumbers are removed from the basket parameters
    Then the basket conatins "6" cucumbers parameters