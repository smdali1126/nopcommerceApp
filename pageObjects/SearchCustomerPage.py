import time

class SearchCustomer:
    # Add Customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tblSearchResults_xpath = "//*[@id='customers-grid']"
    table_xpath = "//*[@id='customers-grid_wrapper']/div[1]/div"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lastname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_element_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[2]").text
            if emailid==email:
                flag = True
                break
            return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr/td[3]").text
            if name == Name:
                flag = True
                break
            return flag
