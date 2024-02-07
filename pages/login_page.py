import allure
from config.base_page import BasePage
from data.links import Links

class LoginPage(BasePage):
    PAGE_URL = Links.STAGE

    LOGIN_FIELD = "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='login-button']"

    @allure.step("Enter login")
    def enter_login(self, login):
        self.find(self.LOGIN_FIELD).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.find(self.PASSWORD_FIELD).send_keys(password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.find(self.LOGIN_BUTTON).click()