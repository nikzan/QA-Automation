from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем два числа и считаем сумму
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    total = str(int(num1) + int(num2))

    # 2. Инициализируем Select и выбираем вариант по значению суммы
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(total)

    # 3. Нажимаем Submit
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

    # 4. Мгновенно забираем код из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
