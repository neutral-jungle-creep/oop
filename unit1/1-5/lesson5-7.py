'''https://stepik.org/lesson/701975/step/9?unit=702076'''
from loguru import logger


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{g.name}: {g.price}' for g in self.goods]


class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Goods):
    pass


class TV(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


cart = Cart()
tv1 = TV("samsung", 1111)
tv2 = TV("LG", 1234)
table = Table("ikea", 2345)
n1= Notebook("msi", 5433)
n2 = Notebook("apple", 542)
c = Cup("keepcup", 43)

cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(n1)
cart.add(n2)
cart.add(c)
cart.remove(0)
print(cart.get_list())