from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import pytest

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckBox().click()
        self.selectOptionByText(homePage.getGender(), getData["gender"])
        homePage.submitForm().click()
        alertText = homePage.getSuccessMessage().text
        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
