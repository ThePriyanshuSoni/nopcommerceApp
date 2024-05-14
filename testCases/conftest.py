from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser......................")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser......................")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser......................")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/Hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


###############  PyTest HTML Report ##################
# It is hook for adding Environment info to HTML Report


def pytest_configure(config):
    config._metadata = {
                        'Project Name': 'nop Commerce',
                        'Module Name': 'Customers',
                        'Tester': 'Priyanshu'
                        }


# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)
