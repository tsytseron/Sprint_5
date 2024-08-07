from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.tests.locators import Locators
from data import user_data

class TestEntrance:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_entrance_log_in_to_account_button(self, driver):
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

    # Вход через кнопку «Личный кабинет»
    def test_entrance_personal_account_button(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.INSCRIPTION_ENTRANCE))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert driver.find_element(*Locators.LOGOUT_BUTTON)

    # Вход через кнопку в форме регистрации
    def test_entrance_registration_form_button(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        button_register = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_HYPERLINK))
        button_register.click()
        driver.find_element(*Locators.LOGIN_HYPERLINK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert driver.find_element(*Locators.LOGOUT_BUTTON)

    # Вход через кнопку в форме восстановления пароля
    def test_entrance_password_recovery_form_button(self, driver):
        login, password = user_data()
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.REGISRATION_HYPERLINK))
        driver.find_element(*Locators.PASSWORD_RECOVERY_HYPERLINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PASSWORD_RECOVERY_LABEL))
        driver.find_element(*Locators.LOGIN_HYPERLINK).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(login)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element_located(Locators.LOGIN_BUTTON))
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        assert driver.find_element(*Locators.LOGOUT_BUTTON)
