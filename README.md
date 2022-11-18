# Sqe-Project
## What is Sylius?

Sylius is an open source ecommerce platform based on the Symfony framework. It’s built from decoupled components that can be used independently in any PHP application even if it doesn’t use Symfony. Then you can decide whether you’ll use the complete platform provided by its creators or take advantage of standalone elements to create a custom solution.

## Why use Sylius ?

1) Scalability: You can deploy Sylius on a single server or in the cloud on a multi-server architecture that is autoscaling. This provides great efficiency for         large projects.

2) Flexibility: You can customize every part of this platform, thanks to its well-thought-out and modern architecture, and the usage of the Symfony framework.

3) Possibility to apply it on multiple devices: You can easily create native mobile apps for iOS, Android, or a progressive web app, due to built-in ecommerce            application interfaces in Sylius.

4) Developer friendly: This ecommerce platform ensures the highest code quality, has a strong testing environment and uses Business-Driven Development (BDD).              It means that the tests are written in a business language which accelerates the application’s testing. 

5) Community : There are more than four thousand developers, product owners, and other specialists working with this tool gathered on the Sylius channel on                Slack. You can join them to ask for support or help others in solving their issues.

6) Open source: You can participate in the development of this tool.
        
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
    
### API Testing :
Sylius is an API-first solution. It means that Sylius can be used as a backend for implementing JavaScript ecommerce software like a progressive web application, single-page application, or a native mobile app. You can build an online shop that can be suitable for any size of business - a small, medium, or large enterprise.

In the documentation provided on GitHub and website shows that API testing of Sylius is done in php language .

#### Understading of the code (Customers login feature ):

    public function it_allows_customer_to_log_in(): void     
    {
        $this->loadFixturesFromFiles(['authentication/customer.yaml']);

        $this->client->request(       // an api post request
            'POST',
            '/api/v2/shop/authentication-token',      // url of the api 
            [],
            [],
            self::CONTENT_TYPE_HEADER,        // set the header as per your requirements for response 
            json_encode([                      // data(json format) as input for post request 
                'email' => 'oliver@doe.com',   
                'password' => 'sylius'
            ])
        );

        $response = $this->client->getResponse();    // response var stores the response received 
        
        // confirmation using assertion whether resonse is as expected 
        $this->assertResponse($response, 'shop/log_in_customer_response', Response::HTTP_OK); 
        
    }


In API Testing we have some common steps or any framework used

1) A base url to be concatenated with the API url.
2) Diferent requests (post, get , push , patch)
3) For request.get requires no data to be passed as input ( mostly tokens for session)
4) For request.post requires data to be assed in json format 
5) Response receieved is then used as it is or use selective parts by using jsonpath.
6) As response receieved is also json format so you can use jsoath to et attributes (id, text , name) values and then compare it .
7) Finally  use assertions to conclude if response received is whats expected

## Task 5 : Exploring existing Unit testing on Sylius .
