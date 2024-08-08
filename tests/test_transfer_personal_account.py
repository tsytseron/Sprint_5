from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.tests.locators import Locators
from data import user_data

class TestTransferPersonalAccount:
    # Переход по клику на «Личный кабинет»
    def test_transfer_personal_account(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.SIGN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert driver.find_element(*Locators.LOGOUT_BUTTON)

        # Данный тест полностью дублирует тест "Вход по кнопке «Войти в аккаунт» на главной", но, поскольку, по заданию нужно написать отдельный тест
        # на "Переход по клику на «Личный кабинет»", я создал отдельный файл с ним.

