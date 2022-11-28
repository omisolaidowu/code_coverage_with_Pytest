import sys
sys.path.append(sys.path[0] + "/..")

from locators.locator import registerUser
from setup.setup import testSettings
import unittest
from dotenv import load_dotenv
import os

load_dotenv('.env')

setup = testSettings()

test_register = registerUser(setup.driver)

E_Commerce_palygroud_URL = "https:"+os.getenv("E_Commerce_palygroud_URL")

class test_registration(unittest.TestCase):
    

    def it_should_register_user(self):
        
        setup.testSetup()
        test_register.test_getWeb(E_Commerce_palygroud_URL)
        title = test_register.test_getTitle()

        self.assertIn("Register", title, "Register is not in title")
        
        test_register.test_fillFirstName("Idowu")
        test_register.test_fillLastName("Omisola")

        test_register.test_fillEmail("testrs@gmail.com") 
        
        test_register.test_fillPhone("090776632")
        test_register.test_fillPassword("12345678")
        test_register.test_fillConfirmPassword("12345678")
        test_register.test_subscribeNo()
        test_register.test_agreeToTerms()
        test_register.test_submit()

        test_register.error_message()
        
        setup.tearDown()