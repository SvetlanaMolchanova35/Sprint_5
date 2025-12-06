import pytest
import time
from pages.main_page import MainPage

class TestConstructor:
    def test_navigate_to_buns_section(self, driver):
        """Переход к разделу 'Булки'"""
        print("\n=== ТЕСТ: Переход к разделу Булки ===")
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        print("1. Переход к разделу Соусы...")
        main_page.go_to_sauces_section()
        time.sleep(1)  # Ждем активации раздела
        
        print("2. Переход к разделу Булки...")
        main_page.go_to_buns_section()
        time.sleep(1)  # Ждем активации раздела
        
        # Проверить активный раздел
        active_section = main_page.get_active_section_text()
        print(f"   Активный раздел: {active_section}")
        
        # Более гибкая проверка
        assert "Булки" in active_section, f"Ожидался раздел 'Булки', получен: '{active_section}'"
        print("✅ Раздел 'Булки' активен")
    
    def test_navigate_to_sauces_section(self, driver):
        """Переход к разделу 'Соусы'"""
        print("\n=== ТЕСТ: Переход к разделу Соусы ===")
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        print("Переход к разделу Соусы...")
        main_page.go_to_sauces_section()
        time.sleep(1)  # Ждем активации раздела
        
        active_section = main_page.get_active_section_text()
        print(f"   Активный раздел: {active_section}")
        
        assert "Соусы" in active_section, f"Ожидался раздел 'Соусы', получен: '{active_section}'"
        print("✅ Раздел 'Соусы' активен")
    
    def test_navigate_to_fillings_section(self, driver):
        """Переход к разделу 'Начинки'"""
        print("\n=== ТЕСТ: Переход к разделу Начинки ===")
        
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        print("Переход к разделу Начинки...")
        main_page.go_to_fillings_section()
        time.sleep(1)  # Ждем активации раздела
        
        active_section = main_page.get_active_section_text()
        print(f"   Активный раздел: {active_section}")
        
        assert "Начинки" in active_section, f"Ожидался раздел 'Начинки', получен: '{active_section}'"
        print("✅ Раздел 'Начинки' активен")