'''https://stepik.org/lesson/701975/step/10?unit=702076'''
from loguru import logger
import sys


class ListObject:
    def __init__(self, data):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.data = data
        self.next_obj = None

    def link(self, obj):
        logger.info(f'Вызов link у класса {self.__class__.__name__}')
        self.next_obj = obj
        logger.info(f'self.next_obj = {obj} {type(obj)}')


lst_in = ['1. Первые шаги в ООП',
          '1.1 Как правильно проходить этот курс',
          '1.2 Концепция ООП простыми словами',
          '1.3 Классы и объекты. Атрибуты классов и объектов',
          '1.4 Методы классов. Параметр self',
          '1.5 Инициализатор init и финализатор del',
          '1.6 Магический метод new. Пример паттерна Singleton',
          '1.7 Методы класса (classmethod) и статические методы (staticmethod)']
head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new



