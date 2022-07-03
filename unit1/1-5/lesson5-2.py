'''https://stepik.org/lesson/701975/step/4?unit=702076'''
from loguru import logger


class Point:
    def __init__(self, x, y, color='black'):
        logger.info(f'вызов __init__ у класса {self.__class__.__name__}')
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2001, 2)]
points[1].color = 'yellow'
logger.info(f'количество объектов в списке = {len(points)}')