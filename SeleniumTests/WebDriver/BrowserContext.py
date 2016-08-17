from selenium import webdriver
from SeleniumTests.ConfigurationProperties import *

class BrowserContext:
    
    def __init__(self, BrowserType): 
        if BrowserType == "Chrome":
            self.WebDriver = webdriver.Chrome()
        
        if BrowserType == "Firefox":
            self.WebDriver = webdriver.Firefox()
        
        if BrowserType == "IE":
            self.WebDriver = webdriver.Ie(ieWebdriverPathAndExecutable)
            