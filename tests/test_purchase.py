import allure
import pytest
from config.base_test import BaseTest
from data.credentials import Credentials


@allure.feature("Purchase")
class TestAddToCard(BaseTest):

    @allure.title("Purchase items")
    @pytest.mark.regression
    def test_purchase(self):
        self.inventory_page.open()
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.click_login_button()
        self.inventory_page.is_opened()
        self.inventory_page.add_backpack()
        self.inventory_page.add_tshirt()
        self.card_page.click_on_card()
        self.card_page.is_opened()
        self.card_page.screenshot("card_items")
        self.card_page.go_to_checkout()
        self.checkout_page.is_opened()
        self.checkout_page.enter_first_name("Olzhas")
        self.checkout_page.enter_last_name("Agubayev")
        self.checkout_page.enter_zip("100600")
        self.checkout_page.click_continue()
        self.review_page.is_opened()
        self.review_page.click_finish()
        self.complete_page.is_opened()
        self.complete_page.screenshot("purchased items")



