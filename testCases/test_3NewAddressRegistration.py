import random
import string
from datetime import time
import selenium.webdriver.support.ui
from pageObjects.NewUserSignup import Login
from pageObjects.NewUserRegistration import Registration
from testCases.test_1NewUserSignUp import random_generator


class Test_003_NewUserRegistration:
    baseURL = "http://a.testaddressbook.com/"
    firstname="George"
    lastname="Smith"
    street="9 Avenue"
    secondary="TestSecondary"
    city="TestCity"
    state="IN"

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
        self.rg.selectNewAddress()
        self.rg.setFirstname(self.firstname)
        self.rg.setLastname(self.lastname)
        self.rg.setAddress1(self.street)
        self.rg.setAddress2(self.secondary)
        self.rg.setCity(self.city)
        self.rg.setdrpvalue(self.state)
        self.rg.setzipcode("1234567")
        self.rg.setCountry("canada")
        #self.rg.setdate()
        self.rg.setage(20)
        self.rg.setwebsite("https://www.google.com/")
        self.rg.setPhone("123456789")
        self.rg.setcolour()
        self.rg.setphoto("C://Users/Bharathi/PycharmProjects/Python/Selenium/AddBook/Screenshots/test_SignIn.png")
        self.rg.setInterest("dance", "read")
        self.rg.setnotes("These are positive values to Register an Address")
        self.rg.clickcreateaddress()
        self.driver.implicitly_wait(10)

        # Verifying the details of the above registration
        results = []

        # Verify firstname
        firstname = self.rg.checkname()
        #print(firstname,self.firstname)
        if firstname == self.firstname:
            results.append("pass")
        else:
            results.append("fail")

        # Verify lastname
        lastname = self.rg.checklastname()
        #print(lastname,self.lastname)
        if lastname == self.lastname:
            results.append("pass")
        else:
            results.append("fail")

        # Verify StreetAddress
        street=self.rg.checkstreet()
        #print(street,self.street)
        if street==self.street:
            results.append("pass")
        else:
            results.append("fail")

        #Verify StreetAddress2
        secondary=self.rg.checksecondaryaddress()
        #print(secondary,self.secondary)
        if secondary==self.secondary:
            results.append("pass")
        else:
            results.append("fail")

        #Verify city
        city=self.rg.checkcity()
        #print(city,self.city)
        if city==self.city:
            results.append("pass")
        else:
            results.append("fail")


        #Verify state
        state=self.rg.checkstate()
        #print(state,self.state)
        if state==self.state:
            results.append("pass")
        else:
            results.append("fail")

        if "fail" not in results:
            assert True
        else:
            assert False
        self.driver.close()



    def test_UserRegistrationIncorrectDetails(self,setup):
        error_text="2 errors prohibited this address from being saved:"
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
        result=[]
        self.rg = Registration(self.driver)
        self.rg.selectAddresses()
        self.rg.selectNewAddress()
        self.rg.setLastname("Brown")
        self.rg.setAddress1("AddressOneMandatory")
        self.rg.setCity("CityMandatory")
        self.rg.clickcreateaddress()
        errmssg=self.rg.checkerror()
        result=[]
        if error_text==errmssg:
            result.append("pass")
        else:
            result.append("fail")
        print(errmssg,result)
        self.rg.setFirstname("Gold")
        self.rg.setzipcode("123456")
        self.rg.clickcreateaddress()

        # Verify firstname
        firstname = self.rg.checkname()
        if firstname == "Gold":
            result.append("pass")
        else:
            result.append("fail")
        print(firstname,result)
        #Verify ZipCode
        zipcode=self.rg.checkzipcode()
        if zipcode=="123456":
            result.append("pass")
        else:
            result.append("fail")
        print(zipcode,result)
        if "fail" not in result:
            assert True
        else:
            assert False
        print(result)
        self.driver.close()
