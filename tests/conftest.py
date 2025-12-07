import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.data_generator import DataGenerator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import REGISTER_URL, LOGIN_URL, DEFAULT_TIMEOUT

@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome"""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def user_data():
    """Генерация тестовых данных пользователя"""
    return {
        "name": DataGenerator.generate_name(),
        "email": DataGenerator.generate_email(),
        "password": DataGenerator.generate_password(6)
    }

@pytest.fixture
def registered_user(driver):
    """Фикстура для регистрации пользователя (БЕЗ входа)"""
    # Генерация тестовых данных
    test_data = {
        "name": DataGenerator.generate_name(),
        "email": DataGenerator.generate_email(),
        "password": DataGenerator.generate_password(6)
    }
    
    # 1. Регистрация
    driver.get(REGISTER_URL)
    
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='name'])[1]"))
    )
    email_input = driver.find_element(By.XPATH, "(//input[@name='name'])[2]")
    password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    
    name_input.send_keys(test_data["name"])
    email_input.send_keys(test_data["email"])
    password_input.send_keys(test_data["password"])
    register_button.click()
    
    # Ждем редиректа на страницу входа
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_contains("login"))
    
    # ВАЖНО: НЕ ВХОДИМ в аккаунт!
    # Просто возвращаем данные для входа
    return test_data

@pytest.fixture
def logged_in_user(driver):
    """Фикстура для регистрации и входа пользователя (для тестов, где нужен вход)"""
    # Генерация тестовых данных
    test_data = {
        "name": DataGenerator.generate_name(),
        "email": DataGenerator.generate_email(),
        "password": DataGenerator.generate_password(6)
    }
    
    # 1. Регистрация
    driver.get(REGISTER_URL)
    
    name_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "(//input[@name='name'])[1]"))
    )
    email_input = driver.find_element(By.XPATH, "(//input[@name='name'])[2]")
    password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    
    name_input.send_keys(test_data["name"])
    email_input.send_keys(test_data["email"])
    password_input.send_keys(test_data["password"])
    register_button.click()
    
    # Ждем редиректа на страницу входа
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_contains("login"))
    
    # 2. Вход
    driver.get(LOGIN_URL)
    
    email_input = WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )
    password_input = driver.find_element(By.XPATH, "//input[@name='Пароль']")
    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    
    email_input.send_keys(test_data["email"])
    password_input.send_keys(test_data["password"])
    login_button.click()
    
    # Ждем входа - появление кнопки "Оформить заказ"
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )
    
    return test_data

@pytest.fixture
def login_page(driver):
    """Фикстура для страницы входа"""
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def main_page(driver):
    """Фикстура для главной страницы"""
    from pages.main_page import MainPage
    return MainPage(driver)

@pytest.fixture
def registration_page(driver):
    """Фикстура для страницы регистрации"""
    from pages.registration_page import RegistrationPage
    return RegistrationPage(driver)