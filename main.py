from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://dzen.ru") # Открываем страницу

assert driver.title == "Дзен", "Страница не открылась"

print("Страница открылась")