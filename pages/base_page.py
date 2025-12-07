from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, DEFAULT_TIMEOUT

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = BASE_URL
    
    def find_element(self, locator, timeout=DEFAULT_TIMEOUT):
        """Найти элемент"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def go_to_site(self):
        """Перейти на базовый URL"""
        self.driver.get(self.base_url)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url