import allure
from config.base_page import BasePage
from data.links import Links

class ReviewPage(BasePage):

    PAGE_URL = Links.REVIEW_PAGE

    FINISH_BUTTON = "//button[@id='finish']"

    @allure.step("Click on Finish button")
    def click_finish(self):
        self.find(self.FINISH_BUTTON).click()