'''https://stepik.org/lesson/701975/step/5?unit=702076'''
from loguru import logger
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


def rand():
    return [random.randint(1, 100) for _ in range(4)]


elements = []

for _ in range(217):
    coord = rand()
    logger.info(f'получены случайные координаты {coord}')
    item = random.choice([Line(*coord), Rect(*coord), Ellipse(*coord)])
    logger.info(f'вызов __init__ у класса {item.__class__.__name__}')
    elements.append(item)

for i in elements:
    if i.__class__.__name__ == 'Line':
        i.ep = 0, 0
        i.sp = 0, 0
        logger.info(f'сброс координат у объекта класса {i.__class__.__name__}')

