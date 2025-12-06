from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    # Поле Имя - первое поле с name='name'
    NAME_INPUT = (By.XPATH, "(//input[@name='name'])[1]")
    
    # Поле Email - второе поле с name='name'  
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    
    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    
    # Кнопка регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Ошибка некорректного пароля (используем класс input__error)
    PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error")
    
    # Ссылка на вход
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")