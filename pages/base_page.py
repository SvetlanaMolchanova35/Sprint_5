from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://stellarburgers.education-services.ru/"
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не найден: {locator}"
        )
    
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def go_to_site(self):
        self.driver.get(self.base_url)
    
    def get_current_url(self):
        return self.driver.current_url
