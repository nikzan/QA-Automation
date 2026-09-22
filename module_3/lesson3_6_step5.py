import math
import os
import time
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()


@pytest.fixture(scope="function")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordCheck")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://stepik.org/login")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.element_to_be_clickable((By.ID, "id_login_email"))).send_keys(os.getenv("STEPIK_LOGIN"))
    driver.find_element(By.ID, "id_login_password").send_keys(os.getenv("STEPIK_PASSWORD"))
    driver.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img")))

    yield driver
    driver.quit()


links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]


@pytest.mark.parametrize("link", links)
def test_alien_message(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 15)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint, textarea")))

    hints = browser.find_elements(By.CSS_SELECTOR, "p.smart-hints__hint")
    if hints and hints[0].is_displayed() and hints[0].text.strip():
        feedback_text = hints[0].text.strip()
    else:
        textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea:not([disabled])")))
        textarea.clear()
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)

        submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission:not([disabled])")))
        submit_btn.click()

        feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint")))
        feedback_text = feedback.text.strip()

    assert feedback_text == "Correct!", f"Расхождение: {feedback_text}"
