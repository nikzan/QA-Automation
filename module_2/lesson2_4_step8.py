import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждем, пока цена не станет ровно $100 (тайм-аут 15 секунд)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Как только цена стала $100 — жмем Book
    browser.find_element(By.ID, "book").click()

    # 3. Считываем x и считаем математическую функцию
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 4. Вводим ответ в поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # 5. Скроллим до кнопки Submit и нажимаем её
    solve_btn = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", solve_btn)
    solve_btn.click()

    # 6. Мгновенно забираем код из алерта в консоль
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    browser.quit()
