import time
import pytest
from selenium import webdriver
from pageObjects.NewUserSignup import Login
from pageObjects.NewUserRegistration import Registration
from Utilities import XLUtils

class Test_002_UserLoginPage:
    baseURL = "http://a.testaddressbook.com/"
    path = ".//TestData/LoginDetails.xlsx"

    def test_verify_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.clicksignin()
        self.driver.implicitly_wait(10)
        status=[]
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.columns = XLUtils.getColumnCount(self.path, 'Sheet1')
        for i in range(2, self.rows + 1):

            self.user = XLUtils.readData(self.path, 'Sheet1', i, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', i, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', i, 3)
            print(self.rows, i, self.user, self.password)
            # Login with excel credentials
            self.driver.maximize_window()
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            # Getting email id and comparing against actual
            self.driver.implicitly_wait(10)
            print(status)
            if self.exp == "pass":
                actual_email_id = self.driver.find_element_by_xpath("//span[contains(text(),'@gmail.com')]").text
                if actual_email_id==self.user:
                    status.append("pass")
                    self.lp.clicksignout()
                else:
                    status.append("fail")
            elif self.exp=="fail":
                status.append("pass")
                self.driver.implicitly_wait(5)
                self.lp.clicksignin()
        if "fail" in status:
            assert False
        else:
            assert True
        self.driver.close()


