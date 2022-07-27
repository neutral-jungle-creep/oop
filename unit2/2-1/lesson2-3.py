'''https://stepik.org/lesson/701983/step/7?unit=702084'''
from loguru import logger


class Book:
    def __init__(self, author, title, price):
        self.set_author(author)
        self.set_title(title)
        self.set_price(price)

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
logger.info(book.get_title())
logger.info(book.get_author())
logger.info(book.get_price())