import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Addcustomerpage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_searchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("******* ssearchCustomerByName_005 *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("***** Login Successfully *****")
        self.logger.info("***** Starting Search Custome by Name *****")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("***** searching customer by Name *****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)

        status=searchcust.searchCustomerByName("victoria Terces")
        assert True==status
        self.logger.info("***** TC_SsearchCustomerByName_005 Finished *****")

        self.driver.close()


