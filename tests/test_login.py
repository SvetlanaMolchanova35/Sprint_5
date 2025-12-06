import pytest
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.data_generator import DataGenerator
from selenium.webdriver.common.by import By

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Фикстура для регистрации тестового пользователя"""
        self.driver = driver
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.registration_page = RegistrationPage(driver)
        
        # Генерация тестовых данных
        self.test_data = {
            "name": DataGenerator.generate_name(),
            "email": DataGenerator.generate_email(),
            "password": DataGenerator.generate_password(6)
        }
        
        print(f"\n=== РЕГИСТРАЦИЯ ТЕСТОВОГО ПОЛЬЗОВАТЕЛЯ ===")
        print(f"Email: {self.test_data['email']}")
        print(f"Пароль: {self.test_data['password']}")
        
        # Регистрация пользователя напрямую (без Page Objects)
        self.driver.get('https://stellarburgers.education-services.ru/register')
        time.sleep(2)
        
        # Заполняем форму регистрации напрямую
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(self.test_data["name"])
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        # Ждем редиректа на страницу входа после регистрации
        time.sleep(4)
        print(f"После регистрации URL: {self.driver.current_url}")
        
        # Возвращаемся на главную страницу для тестов входа
        self.driver.get("https://stellarburgers.education-services.ru/")
        time.sleep(2)
    
    def test_login_from_main_button(self):
        """Вход через кнопку 'Войти в аккаунт' на главной"""
        print(f"\n=== ТЕСТ ВХОДА ЧЕРЕЗ ГЛАВНУЮ КНОПКУ ===")
        print(f"Используем email: {self.test_data['email']}")
        
        # Открыть главную и войти
        self.main_page.go_to_site()
        time.sleep(1)
        
        # DEBUG: Проверим что на главной
        print(f"Перед входом URL: {self.driver.current_url}")
        
        # Вход через Page Object
        self.main_page.click_login_button()
        time.sleep(1)
        
        # DEBUG: Что на странице входа
        print(f"На странице входа URL: {self.driver.current_url}")
        
        # Вход - проверяем метод login()
        self.login_page.login(self.test_data["email"], self.test_data["password"])
        
        # Ждем входа и обновления страницы
        time.sleep(4)
        
        # Проверить успешный вход
        print(f"После входа URL: {self.driver.current_url}")
        
        # Проверяем несколькими способами
        is_logged_in = self.main_page.is_order_button_displayed()
        print(f"1. Метод is_order_button_displayed(): {is_logged_in}")
        
        # Проверяем напрямую
        try:
            order_btn = self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print(f"2. Прямой поиск кнопки: НАЙДЕНА - '{order_btn.text}'")
            direct_check = True
        except:
            print(f"2. Прямой поиск кнопки: НЕ НАЙДЕНА")
            direct_check = False
            
        # Проверяем исчезла ли кнопка входа
        try:
            login_btn = self.driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
            print(f"3. Кнопка 'Войти в аккаунт': ВСЕ ЕЩЕ ЕСТЬ")
        except:
            print(f"3. Кнопка 'Войти в аккаунт': ИСЧЕЗЛА (хорошо)")
        
        # Используем прямую проверку
        assert direct_check, "Кнопка 'Оформить заказ' не отображена после входа"
        print("✅ Вход через главную кнопку успешен")
    
    def test_login_from_personal_account(self):
        """Вход через кнопку 'Личный кабинет'"""
        print(f"\n=== ТЕСТ ВХОДА ЧЕРЕЗ ЛИЧНЫЙ КАБИНЕТ ===")
        print(f"Используем email: {self.test_data['email']}")
        
        self.main_page.go_to_site()
        time.sleep(1)
        
        self.main_page.click_personal_account_button()
        time.sleep(1)
        
        print(f"На странице входа URL: {self.driver.current_url}")
        
        # Вход напрямую (без Page Object)
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Ждем входа
        time.sleep(4)
        
        # Проверяем напрямую
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print("✅ Вход через личный кабинет успешен")
            assert True
        except:
            print(f"❌ Вход не удался. URL: {self.driver.current_url}")
            assert False
    
    def test_login_from_registration_page(self):
        """Вход через кнопку в форме регистрации"""
        print(f"\n=== ТЕСТ ВХОДА СО СТРАНИЦЫ РЕГИСТРАЦИИ ===")
        
        self.main_page.go_to_site()
        time.sleep(1)
        
        self.main_page.click_login_button()
        time.sleep(1)
        
        self.login_page.click_register_link()
        time.sleep(1)
        
        self.registration_page.click_login_link()
        time.sleep(1)
        
        # Вход напрямую
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        time.sleep(4)
        
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print("✅ Вход со страницы регистрации успешен")
            assert True
        except:
            print(f"❌ Вход не удался")
            assert False
    
    def test_login_from_forgot_password_page(self):
        """Вход через кнопку в форме восстановления пароля"""
        print(f"\n=== ТЕСТ ВХОДА СО СТРАНИЦЫ ВОССТАНОВЛЕНИЯ ПАРОЛЯ ===")
        
        self.main_page.go_to_site()
        time.sleep(1)
        
        self.main_page.click_login_button()
        time.sleep(1)
        
        self.login_page.click_forgot_password_link()
        time.sleep(1)
        
        # На странице восстановления нажимаем "Войти"
        self.driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        time.sleep(1)
        
        # Вход напрямую
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        time.sleep(4)
        
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print("✅ Вход со страницы восстановления пароля успешен")
            assert True
        except:
            print(f"❌ Вход не удался")
            assert False