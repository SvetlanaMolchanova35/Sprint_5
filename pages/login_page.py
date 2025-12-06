from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def input_email(self, email):
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
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()