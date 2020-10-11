from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        driver=webdriver.Chrome(executable_path="C:\Users\win10\Downloads\chromedriver_win32 (1)\chromedriver.exe")
        print("Launching Chrome Browser")
    elif browser=='Firefox':
        driver=webdriver.Firefox(executable_path="C:\Users\win10\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe")
        print("Launching Firefox Browser")
    else:
        driver=webdriver.Ie(executable_path="C:\Users\win10\Downloads\IEDriverServer_x64_3.150.1\IEDriverServer.exe")
    return driver

def pytest_addoption(parser): # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # this will return the browser value to setup method
    return request.config.getoption("--browser")

############# Pytest HTML Reports ############

# It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customs'
    config._metadata['Tester'] = 'Ali'

# It is hook for delete / Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


