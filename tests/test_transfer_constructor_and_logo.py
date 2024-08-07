from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.tests.locators import Locators
from data import user_data

class TestTransferConstructorAndLogo:
    # Переход по клику на «Конструктор»
    def test_transfer_constructor_button(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        assert driver.find_element(*Locators.INSCRIPTION_ASSEMBLE_BURGER)

    # Переход по клику на логотип Stellar Burgers
    def test_transfer_logo(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
        assert driver.find_element(*Locators.INSCRIPTION_ASSEMBLE_BURGER)
