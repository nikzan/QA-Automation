import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Кликаем по кнопке (открывается новая вкладка)
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # 2. Переключаемся на вторую открытую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. На новой вкладке считываем x и решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 4. Вводим ответ и жмем Submit
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 5. Мгновенно забираем код из финального алерта
    final_alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", final_alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
