# Sqe-Project
## What is Sylius?

Sylius is an open source ecommerce platform based on the Symfony framework. It’s built from decoupled components that can be used independently in any PHP application even if it doesn’t use Symfony. Then you can decide whether you’ll use the complete platform provided by its creators or take advantage of standalone elements to create a custom solution.

#### About Symmphony Framework

Symfony is one of the most popular PHP web application frameworks in the open-source developers’ community. It uses what is known as Model-View-Controller (MVC) architecture and reusable PHP components to build web applications, APIs, microservices, and web services.
The Symfony framework is a feature-rich and intuitively organized PHP framework that is designed to make it easier for web developers to build scalable and sustainable web applications. But the two most striking pieces of technology that this framework brings to the table are Bundles and Components.

**Bundle** is effectively a plugin — in other words, a small package full of PHP, JavaScript, CSS, image, or Twig files that define a certain functionality or set of functions. Their major benefit comes from the fact that they are decoupled, which allows them to be reconfigured or reused for multiple applications. And, this brings down the overall cost of development.

**Components**, on the other hand, are there to help reduce the work involved in routine tasks. This allows developers to focus on specific features of their application rather than mundane, repetitive tasks. You can add custom modules to use any of these 30 components independently of your main architecture, thereby not harming it in any way. It is even possible to use these components for other PHP frameworks like Laravel or when building a PHP solution from the ground up.

## Why use Sylius ?

1) **Scalability:** You can deploy Sylius on a single server or in the cloud on a multi-server architecture that is autoscaling. This provides great efficiency for         large projects.

2) **Flexibility:** You can customize every part of this platform, thanks to its well-thought-out and modern architecture, and the usage of the Symfony framework.

3) **Possibility to apply it on multiple devices:** You can easily create native mobile apps for iOS, Android, or a progressive web app, due to built-in ecommerce            application interfaces in Sylius.

4) **Developer friendly:** This ecommerce platform ensures the highest code quality, has a strong testing environment and uses Business-Driven Development (BDD).              It means that the tests are written in a business language which accelerates the application’s testing. 

5) **Community :** There are more than four thousand developers, product owners, and other specialists working with this tool gathered on the Sylius channel on                Slack. You can join them to ask for support or help others in solving their issues.

6) **Open source:** You can participate in the development of this tool.

### How could I run the Sylius tests?
To run the phpspec example you just need to clone the project, install vendors through Composer and run a simple command:

        $ bin/phpspec run -fpretty

This should give you a nice output of all specifications, which can also serve as a documentation of classes behavior.

With Behat scenarios, it requires setting up the test database, but then you can simply run:

        $ bin/behat --suite=account
        
## Task 4 : Exploring existing UI and API testing on Sylius .

### UI Testing :


Sylius makes use of BDD. “BDD is a software development process based on test-driven development (TDD). Behavior-driven development combines the general techniques and principles of TDD with ideas from domain-driven design and object-oriented analysis and design to provide software developers and business analysts with shared tools and a shared process to collaborate on software development, with the aim of delivering software that matters.”

Sylius uses the Behat framework to achieve this.

#### Behat
Behat is an open source Behavior-Driven Development framework for PHP. It is a tool to support you in delivering software that matters through continuous communication, deliberate discovery and test-automation.

#### How Behat tests Sylius (few code snippets to explain)

##### A ".feature" extension file that is used to define the test case in gherkin language 

@customer_login //tags
Feature: Signing in to the store                            // line 46 - 49 has no code implementation 
    In order to view my orders
    As a Visitor
    I want to be able to log in to the store

    Background:                                                                     /* runs these lines definitions 
        Given the store operates on a single channel in "United States"                from respective files. In case of Scenrio Outline :  
        And there is a user "ted@example.com" identified by "bear"                      Background runs or before each example *//

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

### Sylius API paths
All paths in new API have the same prefix structure: /api/v2/admin/ or /api/v2/shop/ The /api/v2 prefix part indicates the API version and the /admin/ or /shop/ prefixes are necessary for authorization purposes. When you are adding a new path to API resource configuration, you should remember to add also proper prefix.

You can declare the entire path for each operation (without /api/v2/ as this part is configured globally):

        <collectionOperation name="admin_get">
            <attribute name="method">GET</attribute>
            <attribute name="path">admin/orders</attribute>
        </collectionOperation>
or you can add a proper prefix for all paths in the chosen resource:

<attribute name="route_prefix">shop</attribute>

### Legacy API
Sylius has decided to rebuild their APIs and unify them with API Platform. Previously they had 2 separate APIs for shop (SyliusShopAPi Plugin), and for admin (SyliusAdminApiBundle). Both of them were using the FOSRestBundle, and make operation using commands and events. This approach was easy to understand and implement, but when there is a need to customize something they had to overwrite many files (command, event, command handler, event listener etc). The second reason to create a new Sylius API from scratch is that the API Platform is a modern framework for API and it replaces FOSRestBundle. Sylius will fix security issues in there legacy APIs but all new features will be developed only in the new API.


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


In API Testing we have some common steps for any framework used ...

1) A base url to be concatenated with the API url.
2) Different requests (post, get , push , patch)
3) For request.get requires no data to be passed as input ( mostly tokens for session)
4) For request.post requires data to be assed in json format 
5) Response receieved is then used as it is or use selective parts by using jsonpath.
6) As response receieved is also json format so you can use jsoath to et attributes (id, text , name) values and then compare it .
7) Finally  use assertions to conclude if response received is whats expected

## Task 5 : Exploring existing Unit testing on Sylius .

### PHPUnit
Sylius comes with a lot of PHPUnit functional tests. The configuration file, phpunit.xml.dist, is in the web root and the unit tests are in the tests folder.
In Sylius unit testing is primarily done using PHPUnit and PHPSpec. All the code is wriiten in modular form so that changes can be made easily . Inside the tests folder we see other sub-folders . Following tests/Api/Shop/Customers.php path we get unit tests against this small module that tests the basic functionalities for a customer .

        <?php

        namespace Sylius\Tests\Api\Shop;

        use Sylius\Component\Core\Model\CustomerInterface;
        use Sylius\Tests\Api\JsonApiTestCase;
        use Sylius\Tests\Api\Utils\ShopUserLoginTrait;
        use Symfony\Component\HttpFoundation\Response;

        final class CustomersTest extends JsonApiTestCase       // JsonApiTestCase gets tokens for a session 
        {
            use ShopUserLoginTrait;

            /** @test */
            public function it_returns_small_amount_of_data_on_customer_update(): void
            {
                $loadedData = $this->loadFixturesFromFiles(['authentication/customer.yaml']);
                $token = $this->logInShopUser('oliver@doe.com');

                /** @var CustomerInterface $customer */
                $customer = $loadedData['customer_oliver'];

                $this->client->request(
                    'PUT',
                    '/api/v2/shop/customers/' . $customer->getId(),
                    [],
                    [],
                    [
                        'CONTENT_TYPE' => 'application/ld+json',
                        'HTTP_ACCEPT' => 'application/ld+json',
                        'HTTP_Authorization' => sprintf('Bearer %s', $token)
                    ],
                    json_encode([
                        'firstName' => 'John'
                    ])
                );

                $response = $this->client->getResponse();

                $this->assertResponse($response, 'shop/update_customer_response', Response::HTTP_OK);
            }

            /** @test */
            public function it_registers_customers(): void
            {
                $this->loadFixturesFromFiles(['channel.yaml']);

                $this->client->request(
                    'POST',
                    '/api/v2/shop/customers',
                    [],
                    [],
                    self::CONTENT_TYPE_HEADER,
                    json_encode([
                        'firstName' => 'John',
                        'lastName' => 'Doe',
                        'email' => 'shop@example.com',
                        'password' => 'sylius',
                        'subscribedToNewsletter' => true,
                    ])
                );

                $response = $this->client->getResponse();

                $this->assertResponseCode($response, Response::HTTP_NO_CONTENT);
            }

            /** @test */
            public function it_allows_customer_to_log_in(): void
            {
                $this->loadFixturesFromFiles(['authentication/customer.yaml']);

                $this->client->request(
                    'POST',
                    '/api/v2/shop/authentication-token',
                    [],
                    [],
                    self::CONTENT_TYPE_HEADER,
                    json_encode([
                        'email' => 'oliver@doe.com',
                        'password' => 'sylius'
                    ])
                );

                $response = $this->client->getResponse();

                $this->assertResponse($response, 'shop/log_in_customer_response', Response::HTTP_OK);
            }

            /** @test */
            public function it_allows_customer_to_update_its_data(): void
            {
                $loadedData = $this->loadFixturesFromFiles(['authentication/customer.yaml']);
                $token = $this->logInShopUser('oliver@doe.com');

                /** @var CustomerInterface $customer */
                $customer = $loadedData['customer_oliver'];

                $this->client->request(
                    'PUT',
                    '/api/v2/shop/customers/' . $customer->getId(),
                    [],
                    [],
                    [
                        'CONTENT_TYPE' => 'application/ld+json',
                        'HTTP_ACCEPT' => 'application/ld+json',
                        'HTTP_Authorization' => sprintf('Bearer %s', $token)
                    ],
                    json_encode([
                        'email' => 'john.wick@tarasov.mob',
                        'firstName' => 'John',
                        'lastName' => 'Wick',
                        'gender' => 'm',
                        'subscribedToNewsletter' => true
                    ])
                );

                $response = $this->client->getResponse();

                $this->assertResponse($response, 'shop/updated_gender_customer_response', Response::HTTP_OK);
            }
        }

The above code is pretty simillar to the Api testing code as Sylius makes use of API's to make it lightweight and easier for developers

### According to Sylius Docs
"*In our API based on API Platform framework we have done everything to offer API as easy as possible to use by developer. The most important features of our API:
1)All operations are grouped by shop and admin context (two prefixes)
2)Developers can enable or disable entire API by changing single parameter (check this chapter)
3)We create all endpoints implementing the REST principles and we are using http verbs (POST, GET, PUT, PATCH, DELETE)
4)Returned responses contain minimal information (developer should extend serialization if need more data)
5)Entire business logic is separated from API - if it necessary we dispatch command instead mixing API logic with business logic*"

The unit tests are written in the form of functions to provide modularity , clarity , flexibility and reusability.

All classes with **.php** extension have there respective **ClassNameTest.php** files .
For example the above file code is from Sylius\Tests\Api\Shop\CustomerTest.php file with it class in directory Sylius\Component\Customer\Model\Customer.php
Here the basic functionalities of a Customer are given such as login , personal info updation , register etc . 

## A unit test in the framework 
Assuming that Sylius adds a new feature that has loyalty points for orders placed and then on this basis we have loyalty coupons as well . In such a scenario we will have to make changes to Customer.php file with a function that sums these points each time an order is placed ( an attribute protected $total_order_points; will be added).
A function in Orders.php will also be updated such that it increments the total_order_points for a specific user as soon as the checkout procedure is completed.

for unit  testng we will have the following function in CustomerTest.php

/** @test */
    public function it_counts_customers_total_order_points(): void
    {
        $loadedData = $this->loadFixturesFromFiles(['authentication/customer.yaml']);
        $token = $this->logInShopUser('oliver@doe.com');

        /** @var CustomerInterface $customer */
        $customer = $loadedData['customer_oliver'];
        $points=0;
        $arrlength = count($customer->order_history);

        for($x = 0; $x < $arrlength; $x++) {
          points = points + $customer->order_history[$x].order_points;
        }
        assert($points == $customer->total_order_points , 'The test fails');
    }

