import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем x и вычисляем ответ
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 2. Скроллим страницу на 150px вниз (как в теории этого урока)
    browser.execute_script("window.scrollBy(0, 150);")

    # 3. Вводим ответ в поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # 4. Отмечаем чекбокс и радиокнопку
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    # 5. Кликаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 6. Забираем код из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
