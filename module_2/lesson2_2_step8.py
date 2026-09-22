import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/file_input.html"

# Создаем пустой файл на лету и получаем его абсолютный путь
file_path = os.path.abspath("bio.txt")
with open(file_path, "w") as f:
    f.write("Hello from Arch Linux!")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем обязательные поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@test.ru")

    # 2. Загружаем файл через send_keys в инпут с файлом
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # 3. Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 4. Мгновенно забираем код из алерта
    alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    print("\n" + "=" * 40)
    print("ТВОЙ КОД ДЛЯ STEPIK:", alert.text.split()[-1])
    print("=" * 40 + "\n")

finally:
    # Удаляем временный файл и закрываем браузер
    if os.path.exists(file_path):
        os.remove(file_path)
    browser.quit()
