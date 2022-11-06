Feature: Log In
  Scenario: Verify Log In with valid credentials
    Given launch browser
    When open Sylius Homepage
    And I click Log In
    Then I get redirected to LogIn Page
    When I enter username "shop@example.com" and password "sylius"
    And I click on Log In button
    Then successfully redirected to HomePage verify it by Log Out Option