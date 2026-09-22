from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим все 100 полей по тегу input
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("x")

    # Кликаем на кнопку отправки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Сразу ловим алерт и забираем код без задержек
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
