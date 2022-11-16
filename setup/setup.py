from selenium import webdriver

from dotenv import load_dotenv
import os
load_dotenv('.env')

LT_GRID_USERNAME = os.getenv("LT_GRID_USERNAME")
LT_ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

desired_caps = {
		'LT:Options' : {
			"user" : os.getenv("LT_GRID_USERNAME"),
			"accessKey" : os.getenv("LT_ACCESS_KEY"),
			"build" : "Test Coverage Idowu",
			"name" : "Fireforx coverage demo2",
			"platformName" : os.getenv("TEST_OS")
		},
		"browserName" : "FireFox",
		"browserVersion" : "103.0",
	}
gridURL = "https://{}:{}@hub.lambdatest.com/wd/hub".format(LT_GRID_USERNAME, LT_ACCESS_KEY)

class testSettings: 
       
    def __init__(self) -> None:
        self.driver = webdriver.Remote(command_executor=gridURL, desired_capabilities= desired_caps)
        
    def testSetup(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        if (self.driver != None):
            print("Cleaning the test environment")
            self.driver.quit()