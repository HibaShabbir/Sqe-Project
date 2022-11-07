# Sqe-Project

## Task 4 : Exploring existing UI and API testing on Sylius .

### UI Testing :


Sylius makes use of BDD. “BDD is a software development process based on test-driven development (TDD). Behavior-driven development combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software developers and business analysts with shared tools and a shared process to collaborate on software development, with the aim of delivering software that matters.”

Sylius uses the Behat framework to achieve this.

#### Behat
Behat is an open source Behavior-Driven Development framework for PHP. It is a tool to support you in delivering software that matters through continuous communication, deliberate discovery and test-automation.

#### How Behat tests Sylius (few code snippets to explain)

##### A ".feature" extension file that is used to define the test case in gherkin language 

@customer_login //tags
Feature: Signing in to the store                            /* line 20 - 23 has no code implementation 
    In order to view my orders
    As a Visitor
    I want to be able to log in to the store

    Background:                                                                     /* runs these lines definitions 
        Given the store operates on a single channel in "United States"                from respective files. In case of Scenrio Outline :  
        And there is a user "ted@example.com" identified by "bear"                      Background runs or before each example*/

    @ui @api // tags used
    Scenario: Sign in with email and password
        When I want to log in
        And I specify the username as "ted@example.com"                         //"ted@example" is in quotes as t is a variable
        And I specify the password as "bear"
        And I log in
        Then I should be logged in

##### A ".php" extension file that is used for definition of the steps of the gherkin language 

final class LoginContext implements Context
{
    public function __construct(
        private HomePageInterface $homePage,
        private LoginPageInterface $loginPage
    ) {
    }


@When I want to log in
public function iWantToLogIn()
{
    $this->loginPage->tryToOpen();         //loginPage defined in contructor above
}                                          // tryToOpen() is a function defined in LoginPage.php
                                           //LogInPpage class implements LogInPageInterface 




@When I specify the username as :username
public function iSpecifyTheUsername(?string $username = null): void
{
  $this->loginPage->specifyUsername($username);     //specifyUsername simillarly is function defined in LoginPage class in LoginPage.php 
}

    

@When I specify my password as :password
public function iSpecifyThePasswordAs(?string $password = null): void
{
  $this->loginPage->specifyPassword($password);
}



@When I log in
public function iLogIn(): void
{
  $this->loginPage->logIn();         //loginPage defined in contructor above
}


@Then I should be logged in
public function iShouldBeLoggedIn(): void
{
  $this->homePage->verify();
  Assert::true($this->homePage->hasLogoutButton());   //homePage defined in contructor above
}                                                     // Assert used to show if test passes or fails
