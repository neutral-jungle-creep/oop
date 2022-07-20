'''https://stepik.org/lesson/701978/step/8?unit=702079'''
from loguru import logger
from string import ascii_lowercase, digits


class Input:
    CHARS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя ' + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        if not self.check_name(name):
            raise ValueError("некорректное поле name")
        self.name = name
        self.size = size

    @classmethod
    def check_name(cls, name):
        if 2 < len(name) < 51:
            for i in name:
                if i not in cls.CHARS_CORRECT:
                    return False
        else:
            return False
        return True


class TextInput(Input):
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Input):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.login = lgn
        self.password = psw

    def render_template(self):
        logger.info(f'Вызов render_template у класса {self.__class__.__name__}')
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()