import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.data_generator import DataGenerator
from config import LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from locators.registration_page_locators import RegistrationPageLocators

class TestRegistration:
    def test_successful_registration(self, driver, user_data, main_page, login_page, registration_page):
        """Тест успешной регистрации"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login_page.click_register_link()
        
        # Ждем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_BUTTON)
        )
        
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Ждем редиректа на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        
        # Проверить успешную регистрацию - редирект на страницу входа
        current_url = driver.current_url
        assert LOGIN_URL in current_url, f"Ожидался редирект на {LOGIN_URL}, получен: {current_url}"
    
    def test_registration_short_password_error(self, driver, main_page, login_page, registration_page):
        """Тест ошибки при коротком пароле"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        login_page.click_register_link()
        
        # Ждем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REGISTER_BUTTON)
        )
        
        # Заполнить с коротким паролем (5 символов)
        registration_page.register(
            DataGenerator.generate_name(),
            DataGenerator.generate_email(),
            "12345"  # Всего 5 символов!
        )
        
        # Ждем отображения ошибки
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
        )
        
        # Проверить отображение ошибки
        error_displayed = registration_page.is_password_error_displayed()
        assert error_displayed, "Ошибка короткого пароля не отображена"