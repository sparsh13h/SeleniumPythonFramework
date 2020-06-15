from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        log.info("getting all card titles")
        cards = checkoutPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        checkoutPage.checkoutBtn().click()
        confirmPage = checkoutPage.checkOutItems()
        log.info("Entering country name")
        confirmPage.enterCountry().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.selectCountry().click()
        confirmPage.clickCheckBox().click()
        confirmPage.clickSubmitBtn().click()
        textMatch = confirmPage.alertVerify().text
        log.info("Text received from application is "+textMatch)
        assert ("Success! Thank you!" in textMatch)
