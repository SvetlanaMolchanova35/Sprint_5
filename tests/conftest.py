import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome"""
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Начиная с Selenium 4.6.0, ChromeDriver автоматически управляется
    # Selenium Manager сам найдет и скачает нужный драйвер
    
    # Создание драйвера - Selenium Manager сделает всё автоматически
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    # Закрытие драйвера после теста
    driver.quit()

@pytest.fixture
def user_data():
    """Генерация тестовых данных пользователя"""
    from utils.data_generator import DataGenerator
    return {
        "name": DataGenerator.generate_name(),
        "email": DataGenerator.generate_email(),
        "password": DataGenerator.generate_password(6)
    }