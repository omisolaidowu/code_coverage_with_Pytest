from selenium.webdriver.common.by import By

class element_locator:
    first_name = "//input[@id='input-firstname']"
    last_name = "//input[@id='input-lastname']"
    email = "//input[@id='input-email']"
    telephone = "//input[@id='input-telephone']"
    password = "//input[@id='input-password']"
    confirm_password = "//input[@id='input-confirm']"
    subscribe_no = "//label[@for='input-newsletter-no']"
    agree_terms = "//label[@for='input-agree']"
    submit = "//input[@value='Continue']"
    error_message = "//div[@class='text-danger']"


locator = element_locator()


class registeruser:
    def __init__(self, driver) -> None:
        self.driver=driver
    def error_message(self):
        try:
            return self.driver.find_element(By.XPATH, locator.error_message).text
        except:
            print("Email address passed")
    def test_getWeb(self, URL):
        self.driver.get(URL)
        
    def test_getTitle(self):
        return self.driver.title
    def test_fillFirstName(self, data):
        self.driver.find_element(By.XPATH, locator.first_name).send_keys(data)
    def test_fillLastName(self, data):
        self.driver.find_element(By.XPATH, locator.last_name).send_keys(data)
    def test_fillEmail(self, data):
        self.driver.find_element(By.XPATH, locator.email).send_keys(data)
    def test_fillPhone(self, data):
        self.driver.find_element(By.XPATH, locator.telephone).send_keys(data)
    def test_fillPassword(self, data):
        self.driver.find_element(By.XPATH, locator.password).send_keys(data)
    def test_fillConfirmPassword(self, data):
        self.driver.find_element(By.XPATH, locator.confirm_password).send_keys(data)
    def test_subscribeNo(self):
        self.driver.find_element(By.XPATH, locator.subscribe_no).click()
    def test_agreeToTerms(self):
        self.driver.find_element(By.XPATH, locator.agree_terms).click()
    def test_submit(self):
        self.driver.find_element(By.XPATH, locator.submit).click()
    



