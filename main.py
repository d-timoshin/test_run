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

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise  # Это гарантирует, что тест будет помечен как упавший

    finally:
        # Добавьте скриншот в конце теста, независимо от результата
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)


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

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise  # Это гарантирует, что тест будет помечен как упавший

    finally:
        # Добавьте скриншот в конце теста, независимо от результата
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Geely Motors Website')
@allure.story('Service Booking')
def test_geely_servicebooking(browser):
    try:
        with allure.step("Open Service Booking page"):
            browser.get("https://www.geely-motors.com/for-owners/maintain-and-repair/servicebooking")
            logger.info("Opened Service Booking page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="138"]').click()
            logger.info("Selected car model")

        with allure.step("Enter name"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("servicebooking")
            logger.info("Entered name: servicebooking")

        with allure.step("Enter phone number"):
            phone_input = browser.find_element(By.XPATH, '//*[@id="phone"]')
            phone_input.click()
            phone_input.send_keys(1111111111)
            logger.info("Entered phone number: 1111111111")

        with allure.step("Enter email"):
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
            logger.info("Entered email: prtrol@prtrol.prtrol")

        with allure.step("Check checkboxes"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked all checkboxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.feature('Geely Motors Website')
@allure.story('Get a Quote')
def test_geely_getaquote(browser):
    try:
        with allure.step("Open Get a Quote page"):
            browser.get("https://www.geely-motors.com/forbuyers/getaquote")
            logger.info("Opened Get a Quote page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="348"]').click()
            logger.info("Selected car model")

        with allure.step("Enter personal information"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers getaquote")
            logger.info("Entered name: forbuyers getaquote")

            phone_input = browser.find_element(By.XPATH, '//*[@id="phone"]')
            phone_input.click()
            phone_input.send_keys(1111111111)
            logger.info("Entered phone number: 1111111111")

            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
            logger.info("Entered email: prtrol@prtrol.prtrol")

        with allure.step("Check checkboxes"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[2]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked all checkboxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)


@allure.feature('Geely Motors Website')
@allure.story('Get a Quote')
def test_geely_getaquote(browser):
    try:
        with allure.step("Open Get a Quote page"):
            browser.get("https://www.geely-motors.com/forbuyers/getaquote")
            logger.info("Opened Get a Quote page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="348"]').click()
            logger.info("Selected car model")

        with allure.step("Fill in personal information"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers getaquote")
            browser.find_element(By.XPATH, '//*[@id="phone"]').click()
            browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
            logger.info("Filled in personal information")

        with allure.step("Check required boxes"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[2]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked required boxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.feature('Geely Motors Website')
@allure.story('Customer Support')
def test_geely_customer_support(browser):
    try:
        with allure.step("Open Customer Support page"):
            browser.get("https://www.geely-motors.com/for-owners/customer-support")
            logger.info("Opened Customer Support page")

        with allure.step("Fill in personal information"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("customer-support")
            browser.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("customer-support")
            browser.find_element(By.XPATH, '//*[@id="phone"]').click()
            browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
            browser.find_element(By.XPATH, '//*[@id="vin"]').send_keys("LB37844S18X044933")
            logger.info("Filled in personal information")

        with allure.step("Select support reason"):
            browser.find_element(By.XPATH, '//div[@class="nice-select"]').click()
            browser.find_element(By.XPATH, '//li[@data-value="Благодарность"]').click()
            logger.info("Selected support reason: Благодарность")

        with allure.step("Check required box"):
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            logger.info("Checked required box")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.feature('Geely Motors Website')
@allure.story('Trade-in Policy')
def test_geely_tradeinpolicy(browser):
    try:
        with allure.step("Open Trade-in Policy page"):
            browser.get("https://www.geely-motors.com/forbuyers/tradeinpolicy")
            logger.info("Opened Trade-in Policy page")

        with allure.step("Open form"):
            browser.find_element(By.XPATH, '(//i)[28]').click()
            browser.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-send-btn"]').click()
            logger.info("Opened form")

        with allure.step("Fill in personal information"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("forbuyers tradeinpolicy")
            browser.find_element(By.XPATH, '//*[@id="phone"]').click()
            browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("prtrol@prtrol.prtrol")
            logger.info("Filled in personal information")

        with allure.step("Check required boxes"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked required boxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.feature('Geely Motors Website')
@allure.story('Leasing')
def test_geely_leasing(browser):
    try:
        with allure.step("Open Leasing page"):
            browser.get("https://www.geely-motors.com/forbuyers/leasing/leasingnow")
            logger.info("Opened Leasing page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="411"]').click()
            logger.info("Selected car model")

        with allure.step("Fill in personal information"):
            browser.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("leasing-leasingnow")
            browser.find_element(By.XPATH, '//*[@id="phone"]').click()
            browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
            logger.info("Filled in personal information")

        with allure.step("Check required boxes"):
            browser.find_element(By.XPATH, '(//label[@class="checkbox"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[1]').click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked required boxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)

@allure.feature('Geely Motors Website')
@allure.story('Maximum Benefits')
def test_geely_maximum_benefits(browser):
    try:
        with allure.step("Open Maximum Benefits page"):
            browser.get("https://www.geely-motors.com/forbuyers/specialoffer/maximum-benefits")
            logger.info("Opened Maximum Benefits page")

        with allure.step("Select car model"):
            browser.find_element(By.XPATH, '//div[@class="nice-select   "]').click()
            browser.find_element(By.XPATH, '//li[@data-value="802"]').click()
            logger.info("Selected car model")

        with allure.step("Fill in personal information"):
            browser.find_element(By.XPATH, '(//*[@id="firstName"])[1]').send_keys("maximum-benefits")
            browser.find_element(By.XPATH, '//*[@id="phone"]').click()
            browser.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
            browser.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
            logger.info("Filled in personal information")

        with allure.step("Select dealer"):
            browser.find_element(By.XPATH, '//input[@class="js-dealer-open"]').click()
            browser.find_element(By.XPATH, '(//i)[23]').click()
            browser.find_element(By.XPATH, '//button[@class="primary-button black auto noicon js-dealer-choose"]').click()
            logger.info("Selected dealer")

        with allure.step("Check required boxes"):
            wait = WebDriverWait(browser, 10)
            check_box = (By.XPATH, '(//i[@class="fa fa-check"])[1]')
            wait.until(EC.visibility_of_element_located(check_box))
            browser.find_element(*check_box).click()
            browser.find_element(By.XPATH, '(//i[@class="fa fa-check"])[2]').click()
            logger.info("Checked required boxes")

        with allure.step("Submit form"):
            browser.find_element(By.XPATH, '(//button[@type="submit"])[1]').click()
            logger.info("Submitted form")

        with allure.step("Проверка видимости сообщения об успешной отправке заявки"):
            wait = WebDriverWait(browser, 10)
            SUCCESS_MESSAGE = (By.XPATH, '//span[text()="Заявка успешно отправлена!"]')
            wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))
            logger.info("Сообщение об успешной отправке заявки видимо")

    except Exception as e:
        logger.error(f"Test failed with exception: {str(e)}")
        allure.attach(body=str(e), name="Exception", attachment_type=allure.attachment_type.TEXT)
        raise

    finally:
        allure.attach(browser.get_screenshot_as_png(), name="Final Screenshot", attachment_type=allure.attachment_type.PNG)


    
