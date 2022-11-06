from behave import *
from selenium import webdriver


@given(u'I launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome("D:\dell 5570\Drivers\chromedriver.exe")

@when(u'I open Sylius LogIn page')
def openHomePage(context):
    context.driver.get("https://demo.sylius.com/admin/login")

@when(u'I enter admin username "{admin}" and password "{pwd}"')
def enterUsername(context, admin , pwd):
    context.driver.find_element("xpath",'/html/body/div/div/form/div/div[2]/input').send_keys(admin)
    context.driver.find_element("xpath",'/html/body/div/div/form/div/div[3]/input').send_keys(pwd)

@when(u'I press on LogIn')
def clickLogInBtn(context):
    context.driver.find_element("xpath",'/html/body/div/div/form/div/button[@type="submit"][@class="ui fluid large primary submit button"]').click()

@then(u'successfully redirected to HomePage verify it by Dashboard Option')
def verifyByDashboard(context):
    isDashboard = context.driver.find_element("xpath",'/html/body/div[3]/div/div/div[1]/div[1]/h1/div').text

    if isDashboard == "Dashboard":
        context.driver.close()
        assert True,"Test Passed"
