'''https://stepik.org/lesson/701976/step/10?unit=702077'''
from loguru import logger


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        logger.info(f'Вызов функции clone')
        return Point(self.x, self.y)


pt = Point(1, 2)
logger.info(f'Oбъект имеет свойства:  {pt.x}, {pt.y}')
pt_clone = pt.clone()
logger.info(f'Новый объект имеет свойства:  {pt_clone.x}, {pt_clone.y}')