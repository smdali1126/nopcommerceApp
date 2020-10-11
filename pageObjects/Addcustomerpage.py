import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    # Add Customer Page
    lnkCustomers_menu_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a/span"
    lnkCustomers_menuitem_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a/span"
    btnAddnew_xpath = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"
    txtcustomerRoles_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div/input"
    lstitemAdministrators_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li"
    lstitemGuests_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li"
    listitemVendors_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li"
    lstitemRegistered_xpath = "//*[@id='SelectedCustomerRoleIds_taglist']/li"
    txtAdminContent_xpath = "//*[@id='AdminComment']"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    #txtNewsletter_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div"

    #chkIsTaxexempt_xpath = "//*[@id='IsTaxExempt']"
    #chkActive_xpath = "//*[@id='Active']"
    btnSave_xpath = "/html/body/div[3]/div[3]/div/form/div[1]/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        time.sleep(3)
    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()
    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()
    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstname(self, firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    #def setNewsLetter(self,newsletter):
        #self.driver.find_element_by_xpath(self.txtNewsletter_xpath).send_keys(newsletter)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered / Guests only one
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Registered':
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.lstitem = self.driver.find_element_by_xpath(self.listitemVendors_xpath)
        else:
            self.lstitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        # self.lstitem.click()
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()








