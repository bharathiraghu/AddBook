import random
import string
from datetime import time
import selenium.webdriver.support.ui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.NewUserSignup import Login
from pageObjects.NewUserRegistration import Registration
from pageObjects.DeleteUserDetails import DeleteUser


def checkifelementexists(self, driver):
    try:
        self.driver.find_element_by_link_text("Destroy")
    except NoSuchElementException:
        return False
    return True

class Test_005_DeleteUserRegistration:
    baseURL = "http://a.testaddressbook.com/"

    def test_SignIn(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clicksignin()
        self.driver.implicitly_wait(10)

        # Login with any existing credentials
        self.driver.maximize_window()
        self.lp.setUserName("gi7l82x5@gmail.com")
        self.lp.setPassword("xbgdyob7")
        self.lp.clickLogin()

        # Select Address and Fill in the details for a new User
        self.rg = Registration(self.driver)
        self.rg.selectAddresses()
        self.du=DeleteUser(self.driver)
        elem = self.driver.find_elements_by_link_text("Destroy")
        i=len(elem)
        while i>0:
             self.driver.implicitly_wait(10)
             self.driver.find_element_by_link_text("Destroy").click()
             WebDriverWait(self.driver, 10).until(EC.alert_is_present())
             self.driver.switch_to.alert.accept()
             i-=1
        if len(self.driver.find_elements_by_link_text("Destroy"))==0:
            assert True
        else:
            assert False
        self.driver.quit()



