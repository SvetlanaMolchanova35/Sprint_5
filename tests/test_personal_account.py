import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from config import PROFILE_URL, BASE_URL

class TestPersonalAccount:
    def test_navigate_to_personal_account(self, driver, logged_in_user):
        """Переход в личный кабинет"""
        # Пользователь уже вошел
        
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))
        
        # Проверяем что в личном кабинете
        assert PROFILE_URL in driver.current_url, f"Не перешли в личный кабинет. URL: {driver.current_url}"
    
    def test_navigate_from_personal_account_to_constructor_via_button(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через кнопку 'Конструктор'"""
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))
        
        # Переходим в конструктор через кнопку
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
        
        # Ждем перехода на главную
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        
        # Проверяем что мы на главной странице
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Не перешли на главную страницу"
    
    def test_navigate_from_personal_account_to_constructor_via_logo(self, driver, logged_in_user):
        """Переход из личного кабинета в конструктор через логотип"""
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))
        
        # Переходим в конструктор через логотип
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()
        
        # Ждем перехода на главную
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        
        # Проверяем что мы на главной странице
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Не перешли на главную страницу"