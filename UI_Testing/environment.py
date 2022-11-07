from behave import *
from selenium import webdriver

# before every scenario
def before_scenario(scenario, context):
   print('Before scenario executed')
   #context.driver = webdriver.Chrome("D:\dell 5570\Drivers\chromedriver.exe")
# after every scenario
def after_scenario(scenario, context):
   print('After scenario executed')
  # context.driver.close()