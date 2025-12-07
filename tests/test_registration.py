import time
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.data_generator import DataGenerator
from config import LOGIN_URL

class TestRegistration:
    def test_successful_registration(self, driver, user_data, main_page, login_page, registration_page):
        """Тест успешной регистрации"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        time.sleep(1)
        
        login_page.click_register_link()
        
        # Ждем загрузки страницы регистрации
        time.sleep(1)
        
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Даем время на обработку регистрации
        time.sleep(3)
        
        # Проверить успешную регистрацию - редирект на страницу входа
        current_url = driver.current_url
        assert LOGIN_URL in current_url, f"Ожидался редирект на {LOGIN_URL}, получен: {current_url}"
    
    def test_registration_short_password_error(self, driver, main_page, login_page, registration_page):
        """Тест ошибки при коротком пароле"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        time.sleep(1)
        
        login_page.click_register_link()
        
        # Ждем загрузки страницы регистрации
        time.sleep(1)
        
        # Заполнить с коротким паролем (5 символов)
        registration_page.register(
            DataGenerator.generate_name(),
            DataGenerator.generate_email(),
            "12345"  # Всего 5 символов!
        )
        
        # Даем время на отображение ошибки
        time.sleep(1)
        
        # Проверить отображение ошибки
        error_displayed = registration_page.is_password_error_displayed()
        assert error_displayed, "Ошибка короткого пароля не отображена"