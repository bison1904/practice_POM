import allure
import pytest
from config.base_test import BaseTest
from data.credentials import Credentials

@allure.feature("Social Media Links")
class TestSocialLinks(BaseTest):

    @allure.title("Test LinkedIn link")
    @pytest.mark.new_feature
    def test_linkedin_link(self):
        self.inventory_page.open()
        self.login_page.enter_login(Credentials.LOGIN)
        self.login_page.enter_password(Credentials.PASSWORD)
        self.login_page.click_login_button()
        self.inventory_page.is_opened()
        self.inventory_page.open_linkedin()
        self.redirect_page.is_opened()
        self.redirect_page.screenshot("LinkedIn page")