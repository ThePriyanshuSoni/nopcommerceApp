import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepageTitle(self, setUp):

        self.logger.info("************ Test_001_Login ****************")
        self.logger.info("********* Verifying Home Page Title *************")

        self.driver = setUp
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title Test Pass*************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********* Home Page Title Test Failed *************")

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUp):
        self.logger.info("********* Verifying Login Test*************")

        self.driver = setUp
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("********* Login Test Pass *************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********* Home Page Title Test Failed *************")
            assert False
