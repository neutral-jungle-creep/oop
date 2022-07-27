'''https://stepik.org/lesson/701983/step/5?unit=702084'''
from loguru import logger


class Money:
    def __init__(self, money):
        if Money.check_money(money):
            self.__money = money

    def set_money(self, money):
        self.__init__(money)

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.__money

    @staticmethod
    def check_money(money):
        return isinstance(money, int) and -1 < money


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
logger.info(m1)
m2 = mn_2.get_money()    # 120
logger.info(m2)