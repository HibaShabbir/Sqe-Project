from behave import *
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay= 3

@given(u'I am already logged in from my admin account')
def step_impl(context):
    context.execute_steps('''
                When I open Sylius LogIn page
                And I enter admin username "sylius@example.com" and password "sylius"
                And I press on LogIn
                Then successfully redirected to HomePage verify it by Dashboard Option
            ''')

@when(u'I click on products from Catalog')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/a[2]')))
        element.click()
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I click on +Create button')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[1]/div[2]/div/div')))
        element.click()
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I click on Type Simple Product')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/div[2]/div/div/div/a[1]')))
        element.click()
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I enter code "{code}"')
def step_impl(context, code):
    try:
        context.driver.find_element("xpath",'/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/input').send_keys(code)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I enable channel "{channel}"')
def step_impl(context, channel):
    try:
        element = WebDriverWait(context.driver, delay).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div')))
        element.click()
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I enter Price "{p}" , Original Price "{op}" , Minimum Price "{mp}"')
def step_impl(context , p , op , mp):
    try:
        context.driver.find_element("xpath", '/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/input').send_keys(p)
        context.driver.find_element("xpath", '//*[@id="sylius_product_variant_channelPricings_FASHION_WEB_originalPrice"]').send_keys(op)
        context.driver.find_element("xpath", '/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div/input').send_keys(mp)
        time.sleep(2)
    except:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I enter a name "{name}"')
def step_impl(context, name):
    try:
        context.driver.find_element("xpath",'/html/body/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[1]/input').send_keys(name)
        time.sleep(2)
    except:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@when(u'I press Submit button')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div/div[2]/form/div[3]/button')))
        element.click()
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@then(u'I search the newly created product code "{code}"')
def step_impl(context,code):
    try:
        element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/form/div/input')))
        element.send_keys(code + "\n")
        time.sleep(2)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"


@then(u'results contains the newly added product code "{code}"')
def step_impl(context, code):
    text = context.driver.find_element("xpath",'/html/body/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td[3]').text

    if(text == code):
        context.driver.close()
        assert True, "Test passed"
    else:
        context.driver.close()
        assert False, "Test failed"
