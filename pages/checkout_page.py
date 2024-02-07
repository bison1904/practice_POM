import allure
from config.base_page import BasePage
from data.links import Links

class CheckoutPage(BasePage):

    PAGE_URL = Links.YOUR_INFO_PAGE

    FIRST_NAME_FIELD = "//input[@id='first-name']"
    LAST_NAME_FIELD = "//input[@id='last-name']"
    ZIP_FIELD = "//input[@id='postal-code']"
    CONTINUE_BUTTON = "//input[@type='submit']"

    @allure.step("Enter firstname")
    def enter_first_name(self, firstname):
        self.find(self.FIRST_NAME_FIELD).send_keys(firstname)

    @allure.step("Enter lastname")
    def enter_last_name(self, lastname):
        self.find(self.LAST_NAME_FIELD).send_keys(lastname)

    @allure.step("Enter ZIP code")
    def enter_zip(self, zip):
        self.find(self.ZIP_FIELD).send_keys(zip)

    @allure.step("Click on continue")
    def click_continue(self):
        self.find(self.CONTINUE_BUTTON).click()
