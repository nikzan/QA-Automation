import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Находим сундук и вытаскиваем x из атрибута valuex
    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    # 2. Вводим ответ в поле ввода
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 3. Отмечаем чекбокс "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    # 4. Выбираем radiobutton "Robots rule!"
    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    # 5. Нажимаем кнопку Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

    # 6. Моментально забираем код из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
