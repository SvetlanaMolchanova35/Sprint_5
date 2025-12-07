import random
import string
import time

class DataGenerator:
    @staticmethod
    def generate_email(cohort="99"):
        """Генерация УНИКАЛЬНОГО email"""
        names = ["ivan", "petr", "serg", "alex", "olga", "anna"]
        surnames = ["ivanov", "petrov", "sidorov", "smirnov", "popov"]
        
        name = random.choice(names)
        surname = random.choice(surnames)
        
        # Добавляем временную метку для уникальности
        timestamp = str(int(time.time()))[-6:]  # последние 6 цифр timestamp
        random_chars = ''.join(random.choices(string.ascii_lowercase, k=2))
        
        return f"{name}_{surname}_{cohort}_{timestamp}{random_chars}@yandex.ru"
    
    @staticmethod
    def generate_password(min_length=6):
        """Генерация пароля (минимум 6 символов)"""
        if min_length < 6:
            min_length = 6
        length = random.randint(min_length, 10)
        
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    
    @staticmethod
    def generate_name():
        """Генерация имени"""
        names = ["Иван", "Петр", "Сергей", "Алексей", "Ольга", "Анна"]
        return random.choice(names)