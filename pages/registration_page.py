from .base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage(BasePage):
    def input_name(self, name):
        self.input_text(RegistrationPageLocators.NAME_INPUT, name)

    def input_email(self, email):
        self.input_text(RegistrationPageLocators.EMAIL_INPUT, email)

    def input_password(self, password):
        self.input_text(RegistrationPageLocators.PASSWORD_INPUT, password)

    def click_register_button(self):
        self.click_element(RegistrationPageLocators.REGISTER_BUTTON)

    def click_login_link(self):
        self.click_element(RegistrationPageLocators.LOGIN_LINK)

    def register(self, name, email, password):
        """Заполнение и отправка формы регистрации"""
        self.input_name(name)
        self.input_email(email)
        self.input_password(password)
        self.click_register_button()

    def is_password_error_displayed(self):
        """Проверка отображения ошибки пароля"""
        try:
            # Используем явное ожидание для ошибки
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(RegistrationPageLocators.PASSWORD_ERROR)
            )
            return True
        except Exception:  # Исправлено: было except:
            return False
    
    def get_password_error_text(self):
        """Получение текста ошибки пароля"""
        try:
            error_element = self.find_element(RegistrationPageLocators.PASSWORD_ERROR, timeout=3)
            return error_element.text
        except Exception:  # Исправлено: было except:
            return ""