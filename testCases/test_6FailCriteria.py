from pageObjects.NewUserRegistration import Registration
from pageObjects.NewUserSignup import Login
from testCases.test_3NewAddressRegistration import Test_003_NewUserRegistration


class Test_006_FailCriteria:
    """Create an assertion which will cause a fail
    (e.g. confirm there are three addresses in the list when in fact there are two) and capture a screen-grab on fail.(Logout)"""

    #Generates two new registration entries
    baseURL = "http://a.testaddressbook.com/"


    #Verify the number of elements
    def test_failcase(self,setup):
        #To create 2 new entries for testing purposes
        ar = Test_003_NewUserRegistration()

        #To verify the number of entries
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
        count = self.driver.find_elements_by_link_text("Destroy")
        if len(count)==1:
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_failcase.png")
            self.driver.close()
            assert False
        self.driver.close()




