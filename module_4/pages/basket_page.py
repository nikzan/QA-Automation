from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS_MESSAGE), \
            "Basket is not empty, but should be"
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Products are presented in the basket, but should not be"