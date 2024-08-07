from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import Locators
from data import user_data

class TestLogOutAccount:
    # Выход по кнопке «Выйти» в личном кабинете
    def test_log_out_account(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        logout_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        logout_button.click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        assert driver.find_element(*Locators.LOGIN_BUTTON)
