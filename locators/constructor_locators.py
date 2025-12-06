from selenium.webdriver.common.by import By

class ConstructorLocators:
    # Разделы конструктора (дублируем из main_page для удобства)
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc")