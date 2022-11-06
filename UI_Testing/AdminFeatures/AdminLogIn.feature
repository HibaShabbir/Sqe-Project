Feature: Admin Log In
  Scenario: Verify Log In with valid credentials
    Given I launch browser
    When I open Sylius LogIn page
    And I enter admin username "sylius@example.com" and password "sylius"
    And I press on LogIn
    Then successfully redirected to HomePage verify it by Dashboard Option
