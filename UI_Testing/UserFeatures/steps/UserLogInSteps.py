from behave import *
from selenium import webdriver


@given(u'launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("D:\dell 5570\Drivers\chromedriver.exe")

@when(u'open Sylius Homepage')
def openHomePage(context):
    context.driver.get("https://demo.sylius.com/en_US/")

@when(u'I click Log In')
def clickLogIn(context):
    context.driver.find_element("xpath",'//a[@href= "/en_US/login"]').click()

@then(u'I get redirected to LogIn Page')
def openLogInPage(context):
    context.driver.get("https://demo.sylius.com/en_US/login")

@when(u'I enter username "{user}" and password "{pwd}"')
def enterUsername(context, user , pwd):
    context.driver.find_element("id","_username").send_keys(user)
    context.driver.find_element("id","_password").send_keys(pwd)

@when(u'I click on Log In button')
def clickLogInBtn(context):
    context.driver.find_element("xpath",'//button[@type="submit"][@class="ui blue submit button"]').click()

@then(u'successfully redirected to HomePage verify it by Log Out Option')
def verifyLogoutOption(context):
    isLogout = context.driver.find_element("xpath",'//a[@href="/en_US/logout"][@class="item sylius-logout-button"]').text

    if isLogout == "Logout":
        assert True,"Test Passed"

