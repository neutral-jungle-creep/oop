'''https://stepik.org/lesson/701976/step/8?unit=702077'''
from loguru import logger


class SingletonFive:
    __instance = []

    def __new__(cls, *args, **kwargs):
        logger.info('Вызов функции __new__')
        if len(cls.__instance) < 5:
            logger.info(f'Длина __instance == {len(cls.__instance)}')
            cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1]

    def __init__(self, *args):
        logger.info('Вызов функции __init__')
        self.name = args


objs = [SingletonFive(str(n)) for n in range(10)]
logger.info(objs)