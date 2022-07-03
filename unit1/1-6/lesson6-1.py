'''https://stepik.org/lesson/701976/step/7?unit=702077'''
from loguru import logger


class AbstractClass:
    def __new__(cls, *args, **kwargs):
        logger.info('Ошибка: нельзя создавать объекты абстрактного класса')
        return 'Ошибка: нельзя создавать объекты абстрактного класса'


a = AbstractClass()