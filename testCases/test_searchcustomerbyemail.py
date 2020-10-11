import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Addcustomerpage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_searchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("******* searchCustomerByEmail_004 *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successfully *****")
        self.logger.info("***** Starting Add Customer Test *****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("***** searching customer by email *****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)

        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("***** TC_SearchCustomerbyEmail_004 Finished *****")
        self.driver.close()


