from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Sprint_5.locators import Locators

class TestTransitions:
    # Переход к разделу «Булки»
    def test_transition_to_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_SET))
        driver.find_element(*Locators.BUNS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_SET))
        assert driver.find_element(*Locators.BUNS_SET)

    # Переход к разделу «Соусы»
    def test_transition_to_sauce_section(self, driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_SET))
        assert driver.find_element(*Locators.SAUCES_SET)

    # Переход к разделу «Начинки»
    def test_transition_to_fillings_section(self, driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_SET))
        assert driver.find_element(*Locators.FILLINGS_SET)