import allure
from libs.helper import Helper
from selenium.webdriver.support import expected_conditions as EC

class BasePage(Helper):

    OPEN_MENU = "//button[@id='react-burger-menu-btn']"
    SHOPPING_CARD = "//a[@class='shopping_cart_link']"
    LINKEDIN_BUTTON = "//li[@class='social_linkedin']/a"

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))


