from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    # Раздел "Профиль" в личном кабинете
    PROFILE_INFO = (By.XPATH, "//a[text()='Профиль']")
    
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")