from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ссылка на первую (правильную) страницу
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    # Используем уникальные селекторы (по атрибутам, а не по порядку)

    # Поле "Имя" (First name)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys("Ivan")

    # Поле "Фамилия" (Last name)
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys("Petrov")

    # Поле "Email"
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys("test@test.com")

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что появилось сообщение об успешной регистрации
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # Если тест прошел успешно, выводим сообщение
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Тест на registration1.html прошел успешно!")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
