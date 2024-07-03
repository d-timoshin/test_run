from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
import logging
from allure_commons.types import AttachmentType
from allure_commons._allure import step as allure_step


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
def test_geely_main_page(browser):
    browser.get("https://www.geely-motors.com/")

    input__name = browser.find_element(By.XPATH, '//*[@id="firstName"]')
    input__name.send_keys("news")

    input__email = browser.find_element(By.XPATH, '//*[@id="email"]')
    input__email.send_keys("test@test.test")

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]')
    check__phone.click()

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]')
    check__phone.click()

    btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
    btn.click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '(//button[@class="primary-button blue auto noicon alert__close"])[1]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON)).click()
    


def test_geely_test_drive(browser):
    browser.get("https://www.geely-motors.com/forbuyers/test-drive")
    input__name = browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    input__name = browser.find_element(By.XPATH, '//li[@data-value="802"]').click()


    input__name = browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("test-drive")

    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)

    check__phone = browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    btn = browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

def test_geely_servicebooking(browser):
    browser.get("https://www.geely-motors.com/for-owners/maintain-and-repair/servicebooking")
    input__name = browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    input__name = browser.find_element(By.XPATH, '//li[@data-value="138"]').click()


    input__name = browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("servicebooking")
    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    input__phone = browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    input__email = browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")

    check__phone = browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

    check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    btn = browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()


    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))


def test_geely_getaquote(browser):
    browser.get("https://www.geely-motors.com/forbuyers/getaquote")

    browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    browser.find_element(By.XPATH, '//li[@data-value="348"]').click()

    browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers getaquote")
    browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")

    browser.find_element(By.XPATH, '(//label[@class="checkbox"])[2]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

def test_geely_customer_support(browser):
    browser.get("https://www.geely-motors.com/for-owners/customer-support")

    browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("customer-support")
    browser.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("customer-support")
    browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
    browser.find_element(By.XPATH, '//*[@id="vin"]').send_keys("LB37844S18X044933")

    browser.find_element(By.XPATH, '//div[@class="nice-select"]').click()
    browser.find_element(By.XPATH, '//li[@data-value="Благодарность"]').click()

    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()

    browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

def test_geely_tradeinpolicy(browser):
    browser.get("https://www.geely-motors.com/forbuyers/tradeinpolicy")

    browser.find_element(By.XPATH, '(//i)[28]').click()
    browser.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-send-btn"]').click()

    browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers tradeinpolicy")
    browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")

    browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

def test_geely_leasing(browser):
    browser.get("https://www.geely-motors.com/forbuyers/leasing/leasingnow")

    browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    browser.find_element(By.XPATH, '//li[@data-value="411"]').click()

    browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("leasing-leasingnow")
    browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")

    browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

def test_geely_maximum_benefits(browser):
    browser.get("https://www.geely-motors.com/forbuyers/specialoffer/maximum-benefits")

    browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
    browser.find_element(By.XPATH, '//li[@data-value="802"]').click()

    browser.find_element(By.XPATH, '(//*[@id="firstName"])[1]').send_keys("maximum-benefits")
    browser.find_element(By.XPATH, '//*[@id="phone"]').click()
    browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
    browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
    browser.find_element(By.XPATH, '//input[@class="js-dealer-open"]').click()

    browser.find_element(By.XPATH, '(//i)[23]').click()

    browser.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-dealer-choose"]').click()

    wait = WebDriverWait(browser, 10)
    DELETE_BUTTON = (By.XPATH, '(//i[@class="fa fa-check"])[1]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
    browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()

    browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()

    DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
    wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
    
    print("Победа")

"""


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.feature('Geely Motors Website')
@allure.story('Main Page Subscription')
def test_geely_main_page(browser):
    try:
        with allure.step("Open Geely Motors main page"):
            browser.get("https://www.geely-motors.com/")
            logger.info("Opened Geely Motors main page")

        with allure.step("Enter name"):
            input__name = browser.find_element(By.XPATH, '//*[@id="firstName"]')
            input__name.send_keys("news")
            logger.info("Entered name: news")

        with allure.step("Enter email"):
            input__email = browser.find_element(By.XPATH, '//*[@id="email"]')
            input__email.send_keys("test@test.test")
            logger.info("Entered email: test@test.test")

        with allure.step("Check first checkbox"):
            check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]')
            check__phone.click()
            logger.info("Checked first checkbox")

        with allure.step("Check second checkbox"):
            check__phone = browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]')
            check__phone.click()
            logger.info("Checked second checkbox")

        with allure.step("Click submit button"):
            btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
            btn.click()
            logger.info("Clicked submit button")

        with allure.step("Wait for and click delete button"):
            wait = WebDriverWait(browser, 10)
            DELETE_BUTTON = (By.XPATH, '(//button[@class="primary-button blue auto noicon alert__close"])[1]')
            wait.until(EC.visibility_of_element_located(DELETE_BUTTON)).click()
            logger.info("Clicked delete button")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise  # Это гарантирует, что тест будет помечен как упавший

    finally:
        # Добавьте скриншот в конце теста, независимо от результата
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.feature('Geely Motors Website')
@allure.story('Test Drive')
def test_geely_test_drive(browser):
    try:
        with allure.step("Open Test Drive page"):
            browser.get("https://www.geely-motors.com/forbuyers/test-drive")
            logger.info("Opened Test Drive page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="802"]').click()
            logger.info("Selected car model")

        with allure.step("Enter name"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("test-drive")
            logger.info("Entered name: test-drive")

        with allure.step("Enter phone number"):
            phone_input = browser.find_element(By.XPATH, '//*[@id="phone"]')
            phone_input.click()
            phone_input.send_keys(1111111111)
            logger.info("Entered phone number: 1111111111")

        with allure.step("Check first checkbox"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
            logger.info("Checked first checkbox")

        with allure.step("Check second checkbox"):
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            logger.info("Checked second checkbox")

        with allure.step("Check third checkbox"):
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked third checkbox")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Wait for confirmation button"):
            wait = WebDriverWait(browser, 10)
            DELETE_BUTTON = (By.XPATH, '//a[@class="gradient-button button1 black"]')
            wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
            logger.info("Confirmation button is visible")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise  # Это гарантирует, что тест будет помечен как упавший

    finally:
        # Добавьте скриншот в конце теста, независимо от результата
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)