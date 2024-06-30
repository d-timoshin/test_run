from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Keys


# Опции браузера
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument(" --window-size=1920,1080")

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 60, poll_frequency=1)

#ФОС Подписка на новости

driver.get("https://www.geely-motors.com/")


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("news")

input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '//button[@type="submit"]').click()

DELETE_BUTTON = (By.XPATH, '(//button[@class="primary-button blue auto noicon alert__close"])[1]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON)).click()



#Тест драйв
driver.get("https://www.geely-motors.com/forbuyers/test-drive")
input__name = driver.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="802"]').click()


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("test-drive")

input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)

check__phone = driver.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))



#Записаться на сервис
driver.get("https://www.geely-motors.com/for-owners/maintain-and-repair/servicebooking")
input__name = driver.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="138"]').click()


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("servicebooking")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")

check__phone = driver.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#Получить предложение
driver.get("https://www.geely-motors.com/forbuyers/getaquote")

input__name = driver.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="348"]').click()

input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers getaquote")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")

check__phone = driver.find_element(By.XPATH, '(//label[@class="checkbox"])[2]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС 	Связаться с нами

driver.get("https://www.geely-motors.com/for-owners/customer-support")


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("customer-support")
input__name = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("customer-support")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
input__vin = driver.find_element(By.XPATH, '//*[@id="vin"]').send_keys("LB37844S18X044933")

input__name = driver.find_element(By.XPATH, '//div[@class="nice-select"]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="Благодарность"]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС 	Трейд-ин
driver.get("https://www.geely-motors.com/forbuyers/tradeinpolicy")

input__name = driver.find_element(By.XPATH, '(//i)[28]').click()
input__name = driver.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-send-btn"]').click()

input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers tradeinpolicy")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")


check__phone = driver.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС 	Лизинг

driver.get("https://www.geely-motors.com/forbuyers/leasing/leasingnow")

input__name = driver.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="411"]').click()

input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("leasing-leasingnow")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")


check__phone = driver.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС 	ПОЛУЧИТЕ ВАШЕ ПЕРСОНАЛЬНОЕ ПРЕДЛОЖЕНИЕ НА АВТОМОБИЛЬ GEELY

driver.get("https://www.geely-motors.com/forbuyers/specialoffer/maximum-benefits")

input__name = driver.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
input__name = driver.find_element(By.XPATH, '//li[@data-value="802"]').click()

input__name = driver.find_element(By.XPATH, '(//*[@id="firstName"])[1]').send_keys("maximum-benefits")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
input__dealer = driver.find_element(By.XPATH, '//input[@class="js-dealer-open"]').click()

check__phone = driver.find_element(By.XPATH, '(//i)[23]').click()

check__phone = driver.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-dealer-choose"]').click()

DELETE_BUTTON = (By.XPATH, '(//i[@class="fa fa-check"])[1]')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

check__phone = driver.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

btn = driver.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
print("Победа")