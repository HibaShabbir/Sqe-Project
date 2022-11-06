Feature: Change personal info
  Background:
    Given launch browser
    And I am already logged in from my admin account

    Scenario:
      When I click on products from Catalog
      And I click on +Create button
      And I click on Type Simple Product
      And I enter code "01234"
      And I enable channel "Fashion Web Store"
      And I enter Price "100" , Original Price "90" , Minimum Price "80"
      And I enter a name "Soft T-Shirt Blue"
      And I press Submit button
      Then I search the newly created product code "01234"
      And results contains the newly added product code "01234"
