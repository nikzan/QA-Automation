from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# использую создание фейковых рандомных данных для заполнения(вам потребуется установить эту библилотеку для успешного запуска)
from faker import Faker

try:
    # ссылка на старый сайт, где успешное завершение: http://suninjuly.github.io/registration1.html
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    fake = Faker()
    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    input1.send_keys(fake.name())
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    input2.send_keys(fake.name())
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    input3.send_keys(fake.email())

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
