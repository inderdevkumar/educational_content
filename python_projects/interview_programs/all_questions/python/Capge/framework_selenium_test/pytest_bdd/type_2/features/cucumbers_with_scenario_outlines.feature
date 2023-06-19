Feature: Cucumber Basket
  This will be a comment
  As a gardener,
  I like to carry cucmbetrs in my basket.
  One is scenario outlines and other is normal

  Scenario Outline: Add Cucumbers in my basket parameters
    Given The basket has "<initial>" cucumbers parameters
    When "<some>" Cucumbers are added to the basket parameters
    Then the basket conatins "<total>" cucumbers parameters
    Examples: Amounts
      | initial | some | total |
      | 2       | 4    | 6     |
      | 0       | 3    | 10    |
      | 1       | 2    | 3     |
      | 5       | 4    | 9     |



  Scenario: Remove Cucumbers from my basket parameters
    Given The basket has "10" cucumbers parameters
    When "4" Cucumbers are removed from the basket parameters
    Then the basket conatins "6" cucumbers parameters