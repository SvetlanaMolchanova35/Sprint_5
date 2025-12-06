import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.data_generator import DataGenerator

class TestLogout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Фикстура для подготовки теста"""
        self.driver = driver
        
        # Генерация тестовых данных
        self.test_data = {
            "name": DataGenerator.generate_name(),
            "email": DataGenerator.generate_email(),
            "password": DataGenerator.generate_password(6)
        }
        
        print(f"\n=== ПОДГОТОВКА ТЕСТА ВЫХОДА ===")
        print(f"Email: {self.test_data['email']}")
        
        # 1. Регистрация
        self.driver.get('https://stellarburgers.education-services.ru/register')
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(self.test_data["name"])
        self.driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        time.sleep(4)
        
        # 2. Вход
        self.driver.get('https://stellarburgers.education-services.ru/login')
        time.sleep(2)
        
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(self.test_data["email"])
        self.driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(self.test_data["password"])
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(4)
        
        # 3. Переход в личный кабинет с ожиданием
        print("Переход в личный кабинет...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
        ).click()
        
        # Ждем загрузки личного кабинета
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/account/profile')
        )
        time.sleep(2)
        
        print(f"В личном кабинете. URL: {self.driver.current_url}")
    
    def test_logout(self):
        """Выход из аккаунта"""
        print(f"\n=== ТЕСТ ВЫХОДА ИЗ АККАУНТА ===")
        
        # Ищем и нажимаем кнопку "Выход" с ожиданием
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
        )
        logout_button.click()
        
        # Ждем выхода
        time.sleep(3)
        
        # Проверяем что вышли
        current_url = self.driver.current_url
        print(f"После выхода URL: {current_url}")
        
        # Должны быть на странице входа или главной
        if 'login' in current_url:
            print("✅ Выход успешен: перешли на страницу входа")
            assert True
        else:
            # Проверяем появилась ли кнопка "Войти в аккаунт"
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//button[text()='Войти в аккаунт']"))
                )
                print("✅ Выход успешен: появилась кнопка 'Войти в аккаунт'")
                assert True
            except:
                print(f"❌ Выход не удался. Текущий URL: {current_url}")
                assert False