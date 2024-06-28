from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
# Остальной код...

driver.get("https://dzen.ru") # Открываем страницу

assert driver.title == "Дзен", "Страница не открылась"

print("Страница открылась")