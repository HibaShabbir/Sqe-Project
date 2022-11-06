Feature: Search Items in dress category
  Background:
    Given I launch browser
    And I am logged in as a user
    When I click on dresses category
    Then I get redirected to dresses page

  Scenario Outline: Check Search Items for dresses category with existing keywords
    When I enter existing item keyword "<someKey1>" in search bar
    And I click Search button
    Then I am displayed with items containing keyword "<someKey1>"
    Examples: Credentials
      | someKey1 |
      | strappy  |
      | boho     |
      | wrap     |
      | dress    |
      | null     |

    Scenario Outline: Check Search Items for dresses category with non-existing keywords
    When I enter existing item keyword "<someKey2>" in search bar
    And I click Search button
    Then I am displayed with There are no results to display
    Examples: Credentials
      | someKey2 |
      | lllllll  |
      | 123345   |
      | *****    |