import allure
import pytest
from config.base_test import BaseTest
from data.credentials import Credentials


@allure.feature("Login page")
class TestLogin(BaseTest):

    @allure.title("Login {test_type} scenario")
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "login, password, expected_result, test_type", [
        (Credentials.LOGIN,Credentials.PASSWORD, True,"positive"),(Credentials.LOGIN1,Credentials.PASSWORD1, False,"negative")
    ])
    def test_login_page(self, login, password,expected_result,test_type):
            self.login_page.open()
            self.login_page.enter_login(login)
            self.login_page.enter_password(password)
            self.login_page.click_login_button()
            if expected_result:
                self.inventory_page.is_opened()
