import pytest
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        """Переход к разделу 'Булки'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        
        # Переход сначала к Соусам
        main_page.go_to_sauces_section()
        
        # Ждем активации раздела Соусы
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.ACTIVE_SECTION,
                "Соусы"
            )
        )
        
        # Затем к Букам
        main_page.go_to_buns_section()
        
        # Ждем активации раздела Булки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.ACTIVE_SECTION,
                "Булки"
            )
        )
        
        # Проверить активный раздел
        active_section = main_page.get_active_section_text()
        assert "Булки" in active_section, f"Ожидался раздел 'Булки', получен: '{active_section}'"
    
    def test_navigate_to_sauces_section(self, driver):
        """Переход к разделу 'Соусы'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        
        main_page.go_to_sauces_section()
        
        # Ждем активации раздела Соусы
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.ACTIVE_SECTION,
                "Соусы"
            )
        )
        
        active_section = main_page.get_active_section_text()
        assert "Соусы" in active_section, f"Ожидался раздел 'Соусы', получен: '{active_section}'"
    
    def test_navigate_to_fillings_section(self, driver):
        """Переход к разделу 'Начинки'"""
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        # Ждем загрузки главной страницы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        
        main_page.go_to_fillings_section()
        
        # Ждем активации раздела Начинки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                MainPageLocators.ACTIVE_SECTION,
                "Начинки"
            )
        )
        
        active_section = main_page.get_active_section_text()
        assert "Начинки" in active_section, f"Ожидался раздел 'Начинки', получен: '{active_section}'"