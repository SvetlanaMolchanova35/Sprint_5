from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def click_login_button(self):
        self.click_element(MainPageLocators.LOGIN_BUTTON)
    
    def click_personal_account_button(self):
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        self.click_element(MainPageLocators.LOGO)
    
    def go_to_buns_section(self):
        """Переход к разделу Булки с ожиданием активации"""
        self.click_element(MainPageLocators.BUNS_SECTION)
        # Ждем пока Булки станут активными
        self._wait_for_section_active("Булки")
    
    def go_to_sauces_section(self):
        """Переход к разделу Соусы с ожиданием активации"""
        self.click_element(MainPageLocators.SAUCES_SECTION)
        # Ждем пока Соусы станут активными
        self._wait_for_section_active("Соусы")
    
    def go_to_fillings_section(self):
        """Переход к разделу Начинки с ожиданием активации"""
        self.click_element(MainPageLocators.FILLINGS_SECTION)
        # Ждем пока Начинки станут активными
        self._wait_for_section_active("Начинки")
    
    def get_active_section_text(self):
        """Получение текста активного раздела"""
        element = self.find_element(MainPageLocators.ACTIVE_SECTION)
        return element.text
    
    def is_order_button_displayed(self):
        """Проверка что пользователь вошел (видна кнопка 'Оформить заказ')"""
        try:
            # Используем явное ожидание для надежности
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            return True
        except:
            return False
    
    def _wait_for_section_active(self, section_name):
        """Вспомогательный метод: ожидание активации раздела"""
        try:
            # Ждем максимум 3 секунды
            WebDriverWait(self.driver, 3).until(
                EC.text_to_be_present_in_element(
                    MainPageLocators.ACTIVE_SECTION, 
                    section_name
                )
            )
        except:
            # Если не дождались, всё равно продолжаем
            print(f"Раздел '{section_name}' возможно не активировался")