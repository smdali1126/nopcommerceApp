import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.Addcustomerpage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("******* Test_003_AddCustomer *****")
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

        self.addcust.clickOnAddnew()

        self.logger.info("***** Providing Customer Details *****")

        self.email = random_generator()+ "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("smd@li9916")
        self.addcust.setFirstname("Mohammad")
        self.addcust.setLastname("Ali")
        self.addcust.setGender("Male")
        self.addcust.setDob("7/05/1987")
        self.addcust.setCompanyName("TechMahindra")
        #self.addcust.setNewsLetter("Test store 2")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setAdminContent("This is for Testing Requirement ---------")
        self.addcust.clickOnSave()

        self.logger.info("***** Saving Customer Details *****")
        self.logger.info("***** Add Customer Validation Details *****")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("***** Add Customer Test Pass *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_addcustomer_scr.png")
            self.logger.error("***** Add Customer Test Failed *****")
            assert True == False

        self.driver.close()
        self.logger.info("***** Ending Test_003_AddCustomer Test *****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

