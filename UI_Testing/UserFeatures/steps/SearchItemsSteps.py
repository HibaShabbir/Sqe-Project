from behave import *
from selenium import webdriver
@given(u'I launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome("D:\dell 5570\Drivers\chromedriver.exe")


@given(u'I am logged in as a user')
def step_impl(context):
    context.execute_steps('''
                When open Sylius Homepage
                And I click Log In
                Then I get redirected to LogIn Page
                When I enter username "shop@example.com" and password "sylius"
                And I click on Log In button
                Then successfully redirected to HomePage verify it by Log Out Option
            ''')

@when(u'I click on dresses category')
def step_impl(context):
    context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/a').click()

@then(u'I get redirected to dresses page')
def step_impl(context):
    try:
        text = context.driver.find_element("xpath", '/html/body/div[1]/div[2]/h1').text
    except:
        context.driver.close()
        assert False, "Test failed"+text
    if(text=="Dresses"):
        assert True, "Test passed"



@when(u'I enter existing item keyword "{keyword}" in search bar')
def step_impl(context, keyword):
    if (keyword == "null"):
        keyword = ""
    context.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/form/div/div[1]/div/div/input').send_keys(keyword)


@when(u'I click Search button')
def step_impl(context):
    context.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/form/div/div[2]/div/button').click()


@then(u'I am displayed with items containing keyword "{Key}"')
def step_impl(context, Key):
    parents = context.driver.find_element("xpath",'/html/body/div[1]/div[2]/div[2]/div[2]/div[5]').find_elements("xpath", '*')
    i =1
    for parent in parents:
        text = parent.find_element("xpath", '//*[@id="products"]/div['+str(i)+']/div/a').text
        i = i+1

        if (text.find(Key)):
            print(text)
        else:
            assert False


@then(u'I am displayed with There are no results to display')
def step_impl(context):
    textMsg=context.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/div[2]/div[4]/div/p').text
    if textMsg == "There are no results to display":
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.close()
        assert False, "Test Passed"+textMsg
