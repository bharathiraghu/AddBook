class Login:
    #NewUserCredentials
    textbox_signupusername_id="user_email"
    textbox_signuppassword_id="user_password"
    button_newusersignup_xpath="//input[@name='commit']"
    link_signup_link = "Sign up"
    link_signout_xpath="//a[contains(text(),'Sign out')]"

    #UserCredentials
    textbox_username_id = "session_email"
    textbox_password_id = "session_password"
    button_signup_xpath = "//input[@name='commit']"
    link_signin_id="sign-in"

    # Get driver from test case and initialize it
    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_signup_xpath).click()

    def clicksignin(self):
        self.driver.find_element_by_id(self.link_signin_id).click()

    def clicksignup(self):
        self.driver.find_element_by_link_text(self.link_signup_link).click()

    def setnewusername(self,username):
        self.driver.find_element_by_id(self.textbox_signupusername_id).clear()
        self.driver.find_element_by_id(self.textbox_signupusername_id).send_keys(username)

    def setnewpassword(self,password):
        self.driver.find_element_by_id(self.textbox_signuppassword_id).clear()
        self.driver.find_element_by_id(self.textbox_signuppassword_id).send_keys(password)

    def clicknewusersignup(self):
        self.driver.find_element_by_xpath(self.button_newusersignup_xpath).click()

    def clicksignout(self):
        self.driver.find_element_by_xpath(self.link_signout_xpath).click()