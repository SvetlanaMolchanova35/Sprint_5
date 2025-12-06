from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка входа на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    
    # Кнопка личного кабинета в хедере
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    
    # Кнопка конструктора в хедере
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    
    # Логотип Stellar Burgers
    LOGO = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел конструктора
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")
    
    # Кнопка "Оформить заказ" (видна после входа)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    
    # Ссылка "Войти" в форме восстановления пароля
    LOGIN_LINK_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Войти']")