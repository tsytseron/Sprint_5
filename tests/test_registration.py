from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.tests.locators import Locators
from data import correct_password_user_data, incorrect_password_user_data

class TestRegistration:
    # Успешная регистрация
    def test_successful_registration(self, driver):
        name, login, password = correct_password_user_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        button_register = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_HYPERLINK))
        button_register.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_INSCRIPTION))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert driver.find_element(*Locators.INSCRIPTION_ENTRANCE)

    # Некорректный пароль
    def test_incorrect_password_unsuccessful_registration(self, driver):
        name, login, password = incorrect_password_user_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        button_register = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_HYPERLINK))
        button_register.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_INSCRIPTION))
        driver.find_element(*Locators.INPUT_NAME).send_keys(name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISRATION_BUTTON).click()
        input_error_element = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ERROR_PASSWORD))
        assert input_error_element.text == 'Некорректный пароль'
