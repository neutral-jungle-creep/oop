'''https://stepik.org/lesson/701975/step/3?unit=702076'''
from loguru import logger


class Money:
    def __init__(self, money):
        logger.info(f'вызов __init__ у класса {self.__class__.__name__}')
        self.money = money


my_money = Money(100)
your_money = Money(1000)

