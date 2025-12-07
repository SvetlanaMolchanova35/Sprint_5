from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SHORT_TIMEOUT, DEFAULT_TIMEOUT
import time

class MainPage(BasePage):
    def wait_for_page_load(self):
        """Ожидание полной загрузки главной страницы"""
        # Ждем пока появится кнопка 'Войти в аккаунт' или 'Личный кабинет'
        try:
            self.find_element(MainPageLocators.LOGIN_BUTTON, timeout=15)
        except:
            # Альтернатива: ждем кнопку личного кабинета
            self.find_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON, timeout=15)
    
    def go_to_site(self):
        """Перейти на сайт и дождаться загрузки"""
        self.driver.get(self.base_url)
        self.wait_for_page_load()
    
    def click_login_button(self):
        """Клик по кнопке 'Войти в аккаунт'"""
        self.click_element(MainPageLocators.LOGIN_BUTTON)
    
    def click_personal_account_button(self):
        """Клик по кнопке 'Личный Кабинет'"""
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
    
    def click_constructor_button(self):
        """Клик по кнопке 'Конструктор'"""
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
    
    def click_logo(self):
        """Клик по логотипу Stellar Burgers"""
        self.click_element(MainPageLocators.LOGO)
    
    def go_to_buns_section(self):
        """Переход к разделу 'Булки' с ожиданием активации"""
        self.click_element(MainPageLocators.BUNS_SECTION)
        self._wait_for_section_active("Булки")
    
    def go_to_sauces_section(self):
        """Переход к разделу 'Соусы' с ожиданием активации"""
        self.click_element(MainPageLocators.SAUCES_SECTION)
        self._wait_for_section_active("Соусы")
    
    def go_to_fillings_section(self):
        """Переход к разделу 'Начинки' с ожиданием активации"""
        self.click_element(MainPageLocators.FILLINGS_SECTION)
        self._wait_for_section_active("Начинки")
    
    def get_active_section_text(self):
        """Получение текста активного раздела"""
        element = self.find_element(MainPageLocators.ACTIVE_SECTION)
        return element.text
    
    def is_order_button_displayed(self):
        """Проверка что пользователь вошел (видна кнопка 'Оформить заказ')"""
        try:
            element = WebDriverWait(self.driver, DEFAULT_TIMEOUT).until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
            )
            return element.is_displayed()
        except:
            return False
    
    def _wait_for_section_active(self, section_name):
        """Вспомогательный метод: ожидание активации раздела"""
        WebDriverWait(self.driver, SHORT_TIMEOUT).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.ACTIVE_SECTION, 
                section_name
            )
        )