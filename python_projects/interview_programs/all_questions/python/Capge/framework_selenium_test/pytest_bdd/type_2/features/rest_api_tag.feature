@service @duckduckgo
Feature: Duck duck go Instant Answer API
  As an application developer,
  I want to get instant answers for search terms via a REST API
  So that my app can get answers  anywhere.

  Scenario Outline: Basic DUCK duck go api query
    Given The duckduck go API is queried with "<phrase>"
    Then the response status code is "200"
    And the response contains result for "<phrase>"

    Examples: Animals
      | phrase |
      | panda  |
      | python |
      | tiger  |
      | goat   |
      | murgi  |

    Examples: Fruits
      | phrase |
      | peach  |
      | papaya |
      | apple  |
      | orange |
      | kela   |

