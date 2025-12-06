from .base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalAccountPage(BasePage):
    def click_logout_button(self):
        """Клик по кнопке 'Выход' с явным ожиданием"""
        # Ждем пока кнопка станет кликабельной
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        ).click()
    
    def is_profile_displayed(self):
        """Проверка что открыт личный кабинет (виден раздел 'Профиль')"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_INFO)
            )
            return True
        except:
            return False