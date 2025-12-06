import random
import string

class DataGenerator:
    @staticmethod
    def generate_email(cohort="99"):
        """Генерация email в формате имя_фамилия_номер_когорты_3цифры@домен"""
        names = ["ivan", "petr", "serg", "alex", "olga", "anna"]
        surnames = ["ivanov", "petrov", "sidorov", "smirnov", "popov"]
        
        name = random.choice(names)
        surname = random.choice(surnames)
        digits = ''.join(random.choices(string.digits, k=3))
        
        return f"{name}_{surname}_{cohort}_{digits}@yandex.ru"
    
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