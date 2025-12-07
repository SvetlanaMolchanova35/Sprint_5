import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from config import REGISTER_URL, FORGOT_PASSWORD_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

class TestLogin:
    def test_login_from_main_button(self, driver, registered_user, main_page, login_page):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        login_page.wait_for_page_load()
        
        login_page.login(registered_user["email"], registered_user["password"])
        
        # Проверяем успешный вход
        is_logged_in = main_page.is_order_button_displayed()
        assert is_logged_in, "Вход не выполнен: кнопка 'Оформить заказ' не отображена"
    
    def test_login_from_personal_account(self, driver, registered_user, main_page):
        """Вход через кнопку 'Личный кабинет'"""
        main_page.go_to_site()
        main_page.click_personal_account_button()
        
        # Ждем загрузки страницы логина
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
        )
        
        # Заполняем форму входа с помощью Page Object
        email_input = driver.find_element(By.XPATH, "//input[@name='name']")
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        
        email_input.send_keys(registered_user["email"])
        password_input.send_keys(registered_user["password"])
        login_button.click()
        
        # Проверяем успешный вход
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Вход не выполнен"
    
    def test_login_from_registration_page(self, driver, registered_user, main_page, login_page, registration_page):
        """Вход через кнопку в форме регистрации"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        login_page.wait_for_page_load()
        
        # Переходим на страницу регистрации
        login_page.click_register_link()
        
        # Ждем загрузки страницы регистрации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Зарегистрироваться']"))
        )
        
        # Возвращаемся на страницу логина
        registration_page.click_login_link()
        
        # Ждем загрузки страницы логина
        login_page.wait_for_page_load()
        
        # Заполняем форму входа
        email_input = driver.find_element(By.XPATH, "//input[@name='name']")
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        
        email_input.send_keys(registered_user["email"])
        password_input.send_keys(registered_user["password"])
        login_button.click()
        
        # Проверяем успешный вход
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Вход не выполнен"
    
    def test_login_from_forgot_password_page(self, driver, registered_user, main_page, login_page):
        """Вход через кнопку в форме восстановления пароля"""
        main_page.go_to_site()
        main_page.click_login_button()
        
        # Ждем загрузки страницы логина
        login_page.wait_for_page_load()
        
        # Переходим на страницу восстановления пароля
        login_page.click_forgot_password_link()
        
        # Ждем загрузки страницы восстановления
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[text()='Восстановление пароля']"))
        )
        
        # На странице восстановления нажимаем "Войти"
        login_link = driver.find_element(By.XPATH, "//a[text()='Войти']")
        login_link.click()
        
        # Ждем загрузки страницы логина
        login_page.wait_for_page_load()
        
        # Заполняем форму входа
        email_input = driver.find_element(By.XPATH, "//input[@name='name']")
        password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
        login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
        
        email_input.send_keys(registered_user["email"])
        password_input.send_keys(registered_user["password"])
        login_button.click()
        
        # Проверяем успешный вход
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_button.is_displayed(), "Вход не выполнен"