import allure
from config.base_page import BasePage
from data.links import Links

class CardPage(BasePage):

    PAGE_URL = Links.CARD_PAGE

    CHECKOUT_BUTTON = "//button[@id='checkout']"

    @allure.step("Click on card")
    def click_on_card(self):
        self.find(self.SHOPPING_CARD).click()

    @allure.step("Proceed to checkout")
    def go_to_checkout(self):
        self.find(self.CHECKOUT_BUTTON).click()
