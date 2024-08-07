from selenium.webdriver.common.by import By

class Locators:

    'Шапка и основной контент'
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Конструктор']")
    # Логотип StellarBurgers
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    # Кнопка Личный Кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX']/p[text()='Личный Кабинет']")
    # Надпись СОБЕРИТЕ БУРГЕР
    INSCRIPTION_ASSEMBLE_BURGER = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10' and text()='Соберите бургер']")
    # Кнопка Булки
    BUNS_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Булки"]')
    # Кнопка Соусы
    SAUCES_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Соусы"]')
    # Кнопка Начинки
    FILLINGS_BUTTON = (By.XPATH, '//span[@class="text text_type_main-default" and text()="Начинки"]')
    # Набор булок
    BUNS_SET = (By.XPATH, '//h2[text()="Булки"]')
    # Набор соусов
    SAUCES_SET = (By.XPATH, '//h2[text()="Соусы"]')
    # Набор начинок
    FILLINGS_SET = (By.XPATH, '//h2[text()="Начинки"]')
    # Кнопка Войти в аккаунт
    SIGN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    'Регистрация, авториазция и личный кабинет'
    # Гиперссылка Зарегистрироваться
    REGISRATION_HYPERLINK = (By.XPATH, "// a[text() = 'Зарегистрироваться']")
    # Надпись Регистрация
    REGISRATION_INSCRIPTION = (By.XPATH, "//h2[text()='Регистрация']")
    # Поле Имя
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле Email
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле Пароль
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка Зарегистрироваться
    REGISRATION_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
    # Ошибка некорректного ввода пароля
    ERROR_PASSWORD = (By.XPATH, "//p[@class = 'input__error text_type_main-default']")
    # Надпись Вход
    INSCRIPTION_ENTRANCE = (By.XPATH, "//h2[text() = 'Вход']")
    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Гиперссылка Войти
    LOGIN_HYPERLINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")
    # Надпись Восстановления пароля
    PASSWORD_RECOVERY_LABEL = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Гиперссылка Восстановить пароль
    PASSWORD_RECOVERY_HYPERLINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    # Кнопка Профиль
    PROFILE_BUTTON = (By.XPATH, '//a[@aria-current="page" and text()="Профиль"]')
    # Кнопка Выход
    LOGOUT_BUTTON = (By.XPATH, '//button[@type="button" and text()="Выход"]')
