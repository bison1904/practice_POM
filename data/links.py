import os

class Links:
    STAGE = "https://www.saucedemo.com" if os.environ["STAGE"] == "qa" else " "

    INVENTORY_PAGE = f"{STAGE}/inventory.html"
    CARD_PAGE = f"{STAGE}/cart.html"
    YOUR_INFO_PAGE = f"{STAGE}/checkout-step-one.html"
    REVIEW_PAGE = f"{STAGE}/checkout-step-two.html"
    COMPLETE_PAGE = f"{STAGE}/checkout-complete.html"
    LINKEDIN_PAGE = "https://www.linkedin.com/company/sauce-labs/"
