class DeleteUser:
    link_destroy_linkText="Destroy"

    def __init__(self,driver):
        self.driver=driver

    def clickdestroy(self):
        self.driver.find_element_by_link_text(self.link_destroy_linkText).click()
