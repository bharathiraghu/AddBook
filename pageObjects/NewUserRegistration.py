from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

class Registration:
    txt_Addresses_xpath="//a[contains(text(),'Addresses')]"
    txt_NewAddress_xpath="//a[contains(text(),'New Address')]"
    txt_FirstName_id="address_first_name"
    txt_LastName_id="address_last_name"
    txt_Address1_id="address_street_address"
    txt_Address2_id="address_secondary_address"
    txt_City_id="address_city"
    drpdwn_address_id="address_state"
    txt_zipcode_id='address_zip_code'
    rdbtn_us_id="address_country_us"
    rdbtn_canada_id = "address_country_canada"
    calender_birthday_id="address_birthday"
    slider_color_id='address_color'
    txt_phone_id='address_phone'
    chkbox_climb_id="address_interest_climb"
    chkbox_dance_id="address_interest_dance"
    chkbox_read_id="address_interest_read"
    btn_createaddress_xpath="//input[@value='Create Address']"
    txt_note_id="address_note"
    txt_age_id='address_age'
    txt_website_id='address_website'
    txt_picture_id='address_picture'
    link_edit_xpath="//a[contains(text(),'Edit')]"

    data_firstname_xpath="//span[@data-test='first_name']"
    data_lastname_xpath="//span[@data-test='last_name']"
    data_street_xpath = "//span[@data-test='street_address']"
    data_secondary_xpath="//span[@data-test='secondary_address']"
    data_city_xpath = "//span[@data-test='city']"
    data_state_xpath = "//span[@data-test='state']"
    data_errormssg_xpath="//h4[contains(text(),'2 errors prohibited this address from being saved:')]"
    data_zipcode_xpath="//span[contains(text(),'123456')]"



    def __init__(self, driver):
        self.driver = driver


    def setdrpvalue(self,txt):
        element=self.driver.find_element_by_id(self.drpdwn_address_id)
        drp=Select(element)
        drp.select_by_value(txt)

    def setcolour(self):
        self.driver.execute_script('document.querySelector("#address_color").value="#EC1313";')

    def setdate(self):
        self.driver.find_element_by_id(self.calender_birthday_id).click()



    def selectAddresses(self):
        self.driver.find_element_by_xpath(self.txt_Addresses_xpath).click()

    def selectNewAddress(self):
        self.driver.find_element_by_xpath(self.txt_NewAddress_xpath).click()

    def setFirstname(self,fname):
        self.driver.find_element_by_id(self.txt_FirstName_id).clear()
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys(fname)

    def setLastname(self,lname):
        self.driver.find_element_by_id(self.txt_LastName_id).clear()
        self.driver.find_element_by_id(self.txt_LastName_id).send_keys(lname)

    def setAddress1(self,add1):
        self.driver.find_element_by_id(self.txt_Address1_id).clear()
        self.driver.find_element_by_id(self.txt_Address1_id).send_keys(add1)

    def setAddress2(self,add2):
        self.driver.find_element_by_id(self.txt_Address2_id).clear()
        self.driver.find_element_by_id(self.txt_Address2_id).send_keys(add2)

    def setCity(self,city):
        self.driver.find_element_by_id(self.txt_City_id).clear()
        self.driver.find_element_by_id(self.txt_City_id).send_keys(city)

    def setzipcode(self,zipcode):
        self.driver.find_element_by_id(self.txt_zipcode_id).clear()
        self.driver.find_element_by_id(self.txt_zipcode_id).send_keys(zipcode)

    def setCountry(self,country):
        if country=='us':
            self.driver.find_element_by_id(self.rdbtn_us_id).click()
        elif country=='canada':
            self.driver.find_element_by_id(self.rdbtn_canada_id).click()
        else:
            self.driver.find_element_by_id(self.rdbtn_us_id).click()

    def setBirthday(self,date):
        self.driver.find_element_by_id(self.calender_birthday_id).send_keys(date)

    def setInterest(self,*interest):
        for i in interest:
            if i=='dance':
                self.driver.find_element_by_id(self.chkbox_dance_id).click()
            elif i=='climb':
                self.driver.find_element_by_id(self.chkbox_climb_id).click()
            elif i=='read':
                self.driver.find_element_by_id(self.chkbox_read_id).click()
            else:
                pass

    def setage(self,age):
        self.driver.find_element_by_id(self.txt_age_id).send_keys(age)

    def setPhone(self,phoneno):
        self.driver.find_element_by_id(self.txt_phone_id).send_keys(phoneno)

    def setnotes(self,txt):
        self.driver.find_element_by_id(self.txt_note_id).send_keys(txt)

    def clickcreateaddress(self):
        self.driver.find_element_by_xpath(self.btn_createaddress_xpath).click()

    def setwebsite(self,website):
        self.driver.find_element_by_id(self.txt_website_id).send_keys(website)

    def setphoto(self,filepath):
        self.driver.find_element_by_id(self.txt_picture_id).send_keys(filepath)

    def clickedit(self):
        self.driver.find_element_by_xpath(self.link_edit_xpath).click()

    def checkname(self):
        a=self.driver.find_element_by_xpath(self.data_firstname_xpath).text
        return a

    def checklastname(self):
        b=self.driver.find_element_by_xpath(self.data_lastname_xpath).text
        return b

    def checkstreet(self):
        c=self.driver.find_element_by_xpath(self.data_street_xpath).text
        return c

    def checksecondaryaddress(self):
        d=self.driver.find_element_by_xpath(self.data_secondary_xpath).text
        return d

    def checkcity(self):
        e=self.driver.find_element_by_xpath(self.data_city_xpath).text
        return e

    def checkstate(self):
        f=self.driver.find_element_by_xpath(self.data_state_xpath).text
        return f

    def checkerror(self):
        g=self.driver.find_element_by_xpath(self.data_errormssg_xpath).text
        return g

    def checkzipcode(self):
        h=self.driver.find_element_by_xpath(self.data_zipcode_xpath).text
        return h