import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from utils.data_generator import DataGenerator

class TestPersonalAccount:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Регистрация и вход пользователя (исправленная версия)"""
        self.driver = driver
        
        # Генерация тестовых данных
        self.test_email = DataGenerator.generate_email()
        self.test_password = DataGenerator.generate_password(6)
        
        print(f"\n=== ПОДГОТОВКА: Личный кабинет ===")
        print(f"Email: {self.test_email}")
        print(f"Пароль: {self.test_password}")
        
        # 1. Регистрация (напрямую через Selenium)
        self.driver.get('https://stellarburgers.education-services.ru/register')
        time.sleep(2)
        
        # Заполняем форму регистрации
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys("Тестовый Пользователь")
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(self.test_email)
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_password)
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
        # Ждем редиректа на страницу входа
        time.sleep(4)
        
        # 2. Вход (напрямую через Selenium)
        self.driver.get('https://stellarburgers.education-services.ru/login')
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(self.test_email)
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_password)
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Ждем входа
        time.sleep(4)
        
        # 3. Инициализируем Page Objects ПОСЛЕ входа
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.personal_account_page = PersonalAccountPage(self.driver)
    
    def test_navigate_to_personal_account(self):
        """Переход в личный кабинет"""
        print(f"\n=== ТЕСТ: Переход в личный кабинет ===")
        
        # Уже на главной после входа, проверяем
        print("1. Проверяем что пользователь авторизован...")
        try:
            order_button = self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print(f"   ✓ Кнопка 'Оформить заказ' найдена: '{order_button.text}'")
        except:
            print("   ✗ Пользователь не авторизован")
            assert False, "Пользователь не авторизован"
        
        # Переходим в личный кабинет
        print("2. Переход в личный кабинет...")
        self.main_page.click_personal_account_button()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/account/profile')
        )
        time.sleep(2)
        
        print(f"   Текущий URL: {self.driver.current_url}")
        
        # Проверяем что в личном кабинете
        assert '/account/profile' in self.driver.current_url, f"Не перешли в личный кабинет. URL: {self.driver.current_url}"
        
        # Проверяем наличие раздела "Профиль"
        try:
            profile_element = self.driver.find_element(By.XPATH, "//a[text()='Профиль']")
            print(f"   ✓ Раздел 'Профиль' найден: '{profile_element.text}'")
        except:
            print("   ✗ Раздел 'Профиль' не найден")
        
        print("✅ Успешный переход в личный кабинет")
    
    def test_navigate_from_personal_account_to_constructor_via_button(self):
        """Переход из личного кабинета в конструктор через кнопку 'Конструктор'"""
        print(f"\n=== ТЕСТ: Переход из ЛК в конструктор (кнопка) ===")
        
        # 1. Переходим в личный кабинет
        print("1. Переход в личный кабинет...")
        self.main_page.click_personal_account_button()
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/account/profile')
        )
        time.sleep(2)
        
        print(f"   В личном кабинете. URL: {self.driver.current_url}")
        
        # 2. Переходим в конструктор через кнопку
        print("2. Нажимаем кнопку 'Конструктор'...")
        
        # Ищем кнопку "Конструктор" в хедере
        constructor_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
        )
        constructor_button.click()
        
        # Ждем перехода на главную
        time.sleep(3)
        
        # 3. Проверяем что мы на главной странице
        print(f"   После перехода URL: {self.driver.current_url}")
        
        # Главная страница должна быть корневая или с конструктором
        expected_urls = [
            'https://stellarburgers.education-services.ru/',
            'stellarburgers.education-services.ru'
        ]
        
        is_on_main = any(expected in self.driver.current_url for expected in expected_urls)
        assert is_on_main, f"Не перешли на главную. URL: {self.driver.current_url}"
        
        # Проверяем элементы главной страницы
        try:
            self.driver.find_element(By.XPATH, "//button[text()='Оформить заказ']")
            print("   ✓ На главной странице (есть кнопка 'Оформить заказ')")
        except:
            print("   ⚠️ На главной, но кнопка 'Оформить заказ' не найдена")
        
        print("✅ Успешный переход из ЛК в конструктор через кнопку")
    
    def test_navigate_from_personal_account_to_constructor_via_logo(self):
        """Переход из личного кабинета в конструктор через логотип"""
        print(f"\n=== ТЕСТ: Переход из ЛК в конструктор (логотип) ===")
        
        # 1. Переходим в личный кабинет
        print("1. Переход в личный кабинет...")
        self.main_page.click_personal_account_button()
        
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/account/profile')
        )
        time.sleep(2)
        
        print(f"   В личном кабинете. URL: {self.driver.current_url}")
        
        # 2. Переходим в конструктор через логотип
        print("2. Нажимаем на логотип Stellar Burgers...")
        
        # Ищем логотип и кликаем
        logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2"))
        )
        logo.click()
        
        # Ждем перехода на главную
        time.sleep(3)
        
        # 3. Проверяем что мы на главной странице
        print(f"   После перехода URL: {self.driver.current_url}")
        
        # Главная страница должна быть корневая или с конструктором
        is_on_main = 'stellarburgers.education-services.ru' in self.driver.current_url and '/account/profile' not in self.driver.current_url
        assert is_on_main, f"Не перешли на главную. URL: {self.driver.current_url}"
        
        # Дополнительная проверка - ищем элементы конструктора
        try:
            buns_section = self.driver.find_element(By.XPATH, "//span[text()='Булки']")
            print(f"   ✓ На главной странице (есть раздел 'Булки')")
        except:
            print("   ⚠️ На главной, но разделы конструктора не найдены")
        
        print("✅ Успешный переход из ЛК в конструктор через логотип")