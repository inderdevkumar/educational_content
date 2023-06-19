Feature: Orange HRM Login
  Scenario: Login OrangeHRM Home page
    Given I launch chrome browser
    When I open orange hrm homepage
    And Enter un "Admin" and pass "admin123"
    And click on login button
    And click on User profile
    And click on About
    Then verify if user is sucesffuly logged in and employee number greater than 25
    And close the browser

  Scenario Outline: Login OrangeHRM Home page
    Given I launch chrome browser
    When I open orange hrm homepage
    And Enter un "<username>" and pass "<password>"
    And click on login button
    And click on User profile
    And click on About
    Then verify if user is sucesffuly logged in and employee number greater than 25


    Examples:
      | username | password |
      | admin    | admin123 |
      | admin2   | admin123 |
      | admin3   | admin1234 |
      | admin4   | admin1235 |
      | admin5   | admin1236 |