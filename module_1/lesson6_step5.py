import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# Не ждем тяжелые картинки и CDN, стартуем сразу по готовности DOM
options.page_load_strategy = 'eager'

browser = webdriver.Chrome(options=options)

try:
    browser.get("http://suninjuly.github.io/find_link_text")

    # Считаем формулу и кликаем
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    browser.find_element(By.LINK_TEXT, link_text).click()

    # Заполняем форму
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Быстро ждем алерт и сразу забираем число в консоль
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
