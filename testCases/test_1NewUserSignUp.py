import random
import string

from pageObjects.NewUserSignup import Login


# To generate random alphabets/digits of size 8 to use for emailid/password
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_001_SignIn:
    baseURL = "http://a.testaddressbook.com/"
    username = random_generator() + "@gmail.com"
    password = random_generator()

    # Registering with NewDetails for the first time
    def test_SignUp(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.clicksignin()
        self.driver.implicitly_wait(10)

        # NewUserSignup
        self.lp.clicksignup()
        self.driver.implicitly_wait(10)
        self.lp.setnewusername(self.username)
        self.lp.setnewpassword(self.password)
        self.lp.clicknewusersignup()
        print(self.username, self.password)
        # Getting email id and comparing against actual
        actual_email_id = self.driver.find_element_by_xpath("//span[contains(text(),'@gmail.com')]").text
        if actual_email_id == self.username:
            assert True
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SignIn.png")
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\" + "test_SignIn.png")
        self.lp.clicksignout()
        self.driver.close()


    def test_SignupExisitingCredentials(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.clicksignin()
        self.driver.implicitly_wait(10)

        # NewUserSignup
        self.lp.clicksignup()
        self.driver.implicitly_wait(10)
        self.lp.setnewusername(self.username)
        self.lp.setnewpassword(self.password)
        self.lp.clicknewusersignup()
        actual_title=self.driver.title
        expected_title="Address Book - Sign Up"
        self.driver.implicitly_wait(5)
        if expected_title==actual_title:
            assert True
        else:
            assert False
        self.driver.close()

