import pytest
import time
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        """Переход к разделу 'Булки'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Даем время на полную загрузку
        time.sleep(1)
        
        # Переход сначала к Соусам
        main_page.go_to_sauces_section()
        
        # Даем время на переключение
        time.sleep(1)
        
        # Затем к Букам
        main_page.go_to_buns_section()
        
        # Даем время на переключение
        time.sleep(1)
        
        # Проверить активный раздел
        active_section = main_page.get_active_section_text()
        assert "Булки" in active_section, f"Ожидался раздел 'Булки', получен: '{active_section}'"
    
    def test_navigate_to_sauces_section(self, driver):
        """Переход к разделу 'Соусы'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Даем время на полную загрузку
        time.sleep(1)
        
        main_page.go_to_sauces_section()
        
        # Даем время на переключение
        time.sleep(1)
        
        active_section = main_page.get_active_section_text()
        assert "Соусы" in active_section, f"Ожидался раздел 'Соусы', получен: '{active_section}'"
    
    def test_navigate_to_fillings_section(self, driver):
        """Переход к разделу 'Начинки'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Даем время на полную загрузку
        time.sleep(1)
        
        main_page.go_to_fillings_section()
        
        # Даем время на переключение
        time.sleep(1)
        
        active_section = main_page.get_active_section_text()
        assert "Начинки" in active_section, f"Ожидался раздел 'Начинки', получен: '{active_section}'"