from selenium.webdriver.common.by import By

class LoginPageLocators:
    # Поле Email
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    
    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")