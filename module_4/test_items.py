from selenium.webdriver.common.by import By


def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert len(button) > 0, "Button 'Add to basket' not found on the page"
