from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    country_select = (By.LINK_TEXT, "India")
    primary_Checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    alertmsg = (By.CSS_SELECTOR,"[class*='alert-success']")


    def enterCountry(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.country_select)

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.primary_Checkbox)

    def clickSubmitBtn(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def alertVerify(self):
        return self.driver.find_element(*ConfirmPage.alertmsg)




    #find_element_by_link_text("India")
    #find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
    #driver.find_element_by_css_selector("[type='submit']")
    #self.driver.find_element_by_css_selector("[class*='alert-success']")