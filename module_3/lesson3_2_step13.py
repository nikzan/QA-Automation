import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):
    def fill_form(self, link):
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
            browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("ivan@example.com")

            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            WebDriverWait(browser, 5).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Congratulations")
            )
            welcome_text = browser.find_element(By.TAG_NAME, "h1").text
            return welcome_text
        finally:
            browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
