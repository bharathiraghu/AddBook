import random
import string
from datetime import time
import selenium.webdriver.support.ui
from pageObjects.NewUserSignup import Login
from pageObjects.NewUserRegistration import Registration
from pageObjects.EditUserDetails import EditUser

class Test_004_EditUserRegistration:
    baseURL = "http://a.testaddressbook.com/"

    def test_SignIn(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clicksignin()
        self.driver.implicitly_wait(10)

        #Login with any existing credentials
        self.driver.maximize_window()
        self.lp.setUserName("gi7l82x5@gmail.com")
        self.lp.setPassword("xbgdyob7")
        self.lp.clickLogin()

        #Edit FirstName,State
        self.ed = EditUser(self.driver)
        self.ed.clickAddresses()
        self.ed.clickEditLink()
        self.ed.EditFirstName("EditFirstName")
        self.ed.EditAddressState("California")
        self.ed.Editcolour("#13EC3E")
        results = []
        self.ed.clickupdateAddress()

        # Verify firstname
        self.rg = Registration(self.driver)
        firstname = self.rg.checkname()
        if firstname == "EditFirstName":
            assert True
        else:
            assert False
        self.driver.close()
