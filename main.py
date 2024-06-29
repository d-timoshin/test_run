from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver  # Передаем управление тесту
    driver.quit()  # Закрываем браузер после теста

def test_open_page(browser):  # Принимаем фикстуру как аргумент
    driver = browser  # Получаем экземпляр драйвера из фикстуры

    driver.get("https://dzen.ru")  # Открываем страницу

    assert driver.title == "Дзен", "Страница не открылась"

    print("Страница открылась")