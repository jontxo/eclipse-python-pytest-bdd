import time     
from pytest_bdd import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SeleniumTests.steps.commonSteps import *
from SeleniumTests.WebDriver.BrowserContext import BrowserContext


@given('we have behave installed')
def step_impl():
    print ('first step')
    
@when('we implement a test')
def step_impl1():
    print ('second step')

#     profile = webdriver.FirefoxProfile()
#     time.sleep(5)
#      
#     driver = webdriver.Firefox(profile)
#     driver.get("http://www.python.org")
      
    browser = BrowserContext("IE")
    browser.WebDriver.get("http://www.python.org")
#  
#     fileName = "C:\GIT\eclipse-python_3.5.2-selenium-behave\eclipse-python_3.5.2-selenium-behave\screenshots\image.png"
#     driver.get_screenshot_as_base64()(fileName)
#     print(fileName)
#     print("test")


@then('behave will test it for us!')
def step_impl2():
    addMessage ("third step")
    
@then('behave will test it for us all!')
def step_impl3():
    list = ["1","23","4"]
    print(list[3])
    print ('third step')
    
    