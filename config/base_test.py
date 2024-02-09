from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.card_page import CardPage
from pages.checkout_page import CheckoutPage
from pages.review_page import ReviewPage
from pages.complete_page import CompletePage
from pages.redirect_to_social_media_page import RedirectPages

class BaseTest:
    def setup(self):
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.card_page = CardPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)
        self.review_page = ReviewPage(self.driver)
        self.complete_page = CompletePage(self.driver)
        self.redirect_page = RedirectPages(self.driver)



