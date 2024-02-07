import allure
from config.base_page import BasePage
from data.links import Links

class InventoryPage(BasePage):

    PAGE_URL = Links.INVENTORY_PAGE

    BACKPACK = "//button[@id='add-to-cart-sauce-labs-backpack']"
    TSHIRT ="//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"

    @allure.step("Add backpack to card")
    def add_backpack(self):
        self.find(self.BACKPACK).click()

    @allure.step("Add t-shirt to card")
    def add_tshirt(self):
        self.find(self.TSHIRT).click()

    @allure.step("Open Card page")
    def open_card(self):
        self.find(self.SHOPPING_CARD).click()