from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def wait_for_page_load(self):
        """Ожидание загрузки страницы логина"""
        # Ждем пока поле email станет видимым
        self.find_element(LoginPageLocators.EMAIL_INPUT)
    
    def input_email(self, email):
        # Явное ожидание перед вводом
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
    
    def input_password(self, password):
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
    
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
    
    def click_forgot_password_link(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
    
    def login(self, email, password):
        """Заполнение формы входа и отправка"""
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()