import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators
from locators.login_page_locators import LoginPageLocators
from config import LOGIN_URL, BASE_URL, PROFILE_URL

class TestLogout:
    def test_logout(self, driver, logged_in_user):
        """Выход из аккаунта"""
        # Пользователь уже вошел (благодаря фикстуре logged_in_user)
        
        # Переход в личный кабинет
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(driver, 10).until(EC.url_contains(PROFILE_URL))
        
        # Нажимаем кнопку "Выход"
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        # Ждем выхода - должна быть страница входа
        WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_URL))
        
        # Ждем загрузки страницы логина (появление поля email)
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        assert email_field.is_displayed(), "Не перешли на страницу входа после выхода"
        
        # Дополнительно: проверяем URL
        assert LOGIN_URL in driver.current_url, f"Ожидался URL логина, получен: {driver.current_url}"