from selenium.webdriver.support.select import Select


class EditUser:
    link_Addresses_xpath="//a[contains(text(),'Addresses')]"
    link_edit_linktext= "Edit"
    txtbox_firstname_id='address_first_name'
    drpdown_state_id="address_state"
    link_Update_class="btn btn-primary"
    link_UpdateAddresses_xpath = "//a[contains(text(),'Update Address')]"
    def __init__(self, driver):
        self.driver = driver

    def clickAddresses(self):
        self.driver.find_element_by_xpath(self.link_Addresses_xpath).click()

    def clickEditLink(self):
        self.driver.find_element_by_link_text(self.link_edit_linktext).click()
        # links = self.driver.find_elements_by_link_text(self.link_edit_linktext)
        # print(len(links))
        # for link in links:
        #     self.driver.find_element_by_link_text(self.link_edit_linktext).click()

    def EditFirstName(self,name):
        self.driver.find_element_by_id(self.txtbox_firstname_id).clear()
        self.driver.find_element_by_id(self.txtbox_firstname_id).send_keys(name)

    def EditAddressState(self,state):
            element = self.driver.find_element_by_id(self.drpdown_state_id)
            drp = Select(element)
            drp.select_by_visible_text(state)

    def Editcolour(self,color):
        self.driver.execute_script('document.querySelector("#address_color").value="#13EC3E";')

    def clickUpdate(self):
        self.driver.find_element_by_class_name(self.link_Update_class).click()

    def UpdateAddress(self):
        self.driver.find_element_by_xpath(self.link_Addresses_xpath).click()

