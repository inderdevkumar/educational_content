Feature: Orange HRM Login ie. name of the feature
  Scenario: Logo presence in OrangeHRM Home page
    Given I launch chrome browser
    When I open orange hrm homepage
    Then I verify logo present in the home page
    And close the browser
