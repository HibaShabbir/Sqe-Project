from behave import *
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
delay = 3 # seconds

@given(u'I am already logged in as a user')
def step_impl(context):
    context.execute_steps('''
                When open Sylius Homepage
                And I click Log In
                Then I get redirected to LogIn Page
                When I enter username "shop@example.com" and password "sylius"
                And I click on Log In button
                Then successfully redirected to HomePage verify it by Log Out Option
            ''')

@when(u'I click on a "{subCategory}" from "{category}"')
def step_impl(context , category, subCategory):
    if (category == "Dresses"):
        try:
            element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/a')))
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")
            context.driver.close()
            assert False, "Test failed"
       #context.driver.find_element("xpath",'/html/body/div[1]/div[2]/header/div[4]/a').click()

    elif(category == "T-shirts"):
        try:
            element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[1]')))
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")
            context.driver.close()
            assert False, "Test failed"
        #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[1]').click()
        if (subCategory == "Men"):
            try:
                element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[1]/div/a[1]')))
                element.click()
                time.sleep(3)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath",'/html/body/div[1]/div[2]/header/div[4]/div[1]/div/a[1]').click()
        else:
            try:
                element = WebDriverWait(context.driver, delay).until( EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[1]/div/a[2]')))
                element.click()
                time.sleep(3)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[1]/div/a[2]').click()

    elif (category == "Caps"):
        try:
            element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/header/div[4]/div[2]')))
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")
            context.driver.close()
            assert False, "Test failed"
        #context.driver.find_element("xpath",'/html/body/div[1]/div[2]/header/div[4]/div[2]').click()
        if (subCategory == "Simple"):
            try:
                element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[2]/div/a[1]')))
                element.click()
                time.sleep(3)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[2]/div/a[1]').click()
        else:
            try:
                element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[2]/div/a[2]')))
                element.click()
                time.sleep(5)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[2]/div/a[2]').click()

    elif(category == "Jeans"):
        try:
            element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/header/div[4]/div[3]')))
            element.click()
            time.sleep(3)
        except TimeoutException:
            print("Loading took too much time!")
            context.driver.close()
            assert False, "Test failed"
        #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[3]').click()
        if (subCategory == "Men"):
            try:
                element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[3]/div/a[1]')))
                element.click()
                time.sleep(3)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[3]/div/a[1]').click()
        else:
            try:
                element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/header/div[4]/div[3]/div/a[2]')))
                element.click()
                time.sleep(3)
            except TimeoutException:
                print("Loading took too much time!")
                context.driver.close()
                assert False, "Test failed"
            #context.driver.find_element("xpath", '/html/body/div[1]/div[2]/header/div[4]/div[3]/div/a[2]').click()

@when(u'I click on an "{itemName}"')
def step_impl(context , itemName):
    context.driver.find_element("xpath",'//*[@id="info-toggle"]').click()
    parents = context.driver.find_element("xpath", '/html/body/div[1]/div[2]/div[2]/div[2]/div[5]').find_elements("xpath", '*')
    i = 1
    found = False

    for parent in parents:
        try:
            element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="products"]/div['+str(i)+']/div/a')))
            text = element.text
            element = parent.find_element("xpath", '//*[@id="products"]/div[' + str(i) + ']/div/a')
            text = element.text
            print(str(i) + " " + text)
            if (text == (itemName)):
                print(text)
                element.click()
                found = True
                break
            else:
             i = i + 1
        except TimeoutException:
            print("Loading took too much time!")
            context.driver.close()
            assert False, "Test failed" + text
    if (found == False):
        context.driver.close()
        assert False, "test failed !"



    #context.driver.find_element("xpath",'//a[@href=' + itemBlock + ']').click()

@then(u'details of "{itemName}" page opens')
def step_impl(context, itemName):
    try:
        element = WebDriverWait(context.driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[2]/h1')))
        text = element.text
        print(text)
    except TimeoutException:
        print("Loading took too much time!")
        context.driver.close()
        assert False, "Test failed"+text

    if(text==itemName):
        context.driver.close()
        assert True, "Test passed"
