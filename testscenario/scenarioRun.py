# import coverage
# cov = coverage.Coverage()

# cov.start()



import sys
sys.path.append(sys.path[0] + "/..")

from locators.locator import registeruser
from setup.setup import testSettings
import unittest



setup = testSettings()

test_register = registeruser(setup.driver)


class test_registration(unittest.TestCase):
    

    def test_should_register_user(self):
        setup.testSetup()
        test_register.test_getWeb("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
        title = test_register.test_getTitle()

        self.assertIn("Register", title, "Register is not in title")
        
        test_register.test_fillFirstName("Idowu")
        test_register.test_fillLastName("Omisola")

        # If email address is valid, the try/except block does not run but is tracked since there is no element
        # If email address is invalid, the code in the try block runs but the except one doesn't:
        # Thus, coverage omits this and flags that the Except doesn't run
        test_register.test_fillEmail("testerrs@gmail") 
        
        test_register.test_fillPhone("090776632")
        test_register.test_fillPassword("12345678")
        test_register.test_fillConfirmPassword("12345678")
        test_register.test_subscribeNo()
        test_register.test_agreeToTerms()
        test_register.test_submit()

        test_register.error_message()
        
        setup.tearDown()
    

    




