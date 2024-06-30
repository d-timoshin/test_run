from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()  # Закрываем браузер после теста
"""
def test_dzen_page(browser):
    browser.get("https://dzen.ru")  # Открываем страницу
    assert browser.title == "Дзен", "Страница не открылась"
    print("Открыто")"""

def test_geely_page(browser):

    browser.get("https://www.geely-motors.com/forbuyers/specialoffer/maximum-benefits")

    input__name = browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    input__name = browser.find_element(By.XPATH, '//li[@data-value="802"]').click()

    input__name = browser.find_element(By.XPATH, '(//*[@id="firstName"])[1]').send_keys("maximum-benefits")
    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    input__email = browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
    input__dealer = browser.find_element(By.XPATH, '//input[@class="js-dealer-open"]').click()

    check__phone = browser.find_element(By.XPATH, '(//i)[23]').click()

    check__phone = browser.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-dealer-choose"]').click()

    