from selenium import  webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=".\\Drivers\\" + "chromedriver.exe")
    return  driver


#**************************HTML Report*****************************
def pytest_configure(config):
    config._metadata['Project Name']='Addess Book'
    config._metadata['Module Name']='User Address Registration'
    config._metadata['Tester']='Bharathi Raghavendra'
#********************************************************************


