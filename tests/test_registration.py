import pytest
import time  # Убедитесь что импортировано
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage

class TestRegistration:
    def test_successful_registration(self, driver, user_data):
        """Тест успешной регистрации"""
        print(f"\nТест регистрации с email: {user_data['email']}")

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)

        # Открыть главную и перейти к регистрации
        main_page.go_to_site()
        main_page.click_login_button()
        login_page.click_register_link()

        # Заполнить и отправить форму
        registration_page.register(
            user_data["name"],
            user_data["email"],
            user_data["password"]
        )
        
        # Ждем редирект (увеличиваем время ожидания)
        time.sleep(3)
        
        # Проверить успешную регистрацию - редирект на страницу входа
        current_url = registration_page.get_current_url()
        print(f"Текущий URL после регистрации: {current_url}")
        
        # Более гибкая проверка - может быть /login или что-то еще
        assert 'login' in current_url, f"Ожидался редирект на login, получен: {current_url}"
        print("✅ Регистрация успешна, редирект на страницу входа")
    
    def test_registration_short_password_error(self, driver):
        """Тест ошибки при коротком пароле"""
        from utils.data_generator import DataGenerator

        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        registration_page = RegistrationPage(driver)

        # Открыть главную и перейти к регистрации
        main_page.go_to_site()
        main_page.click_login_button()
        login_page.click_register_link()

        # Заполнить с коротким паролем (5 символов)
        registration_page.register(
            DataGenerator.generate_name(),
            DataGenerator.generate_email(),
            "12345"  # Всего 5 символов!
        )
        
        # Дать время для отображения ошибки
        time.sleep(2)
        
        # Проверить отображение ошибки
        error_displayed = registration_page.is_password_error_displayed()
        print(f"Ошибка пароля отображена: {error_displayed}")
        
        # Если ошибка не отображается, проверим вручную
        if not error_displayed:
            print("Проверяем вручную наличие ошибок на странице...")
            # Можно добавить дополнительную проверку
            try:
                error_elements = driver.find_elements(By.CSS_SELECTOR, '.input__error')
                print(f"Найдено элементов с ошибками: {len(error_elements)}")
                for elem in error_elements:
                    print(f"Текст ошибки: {elem.text}")
            except:
                pass
        
        assert error_displayed, "Ошибка короткого пароля не отображена"
        print("✅ Ошибка короткого пароля корректно отображена")