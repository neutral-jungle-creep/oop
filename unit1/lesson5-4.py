'''https://stepik.org/lesson/701975/step/6?unit=702076'''
from loguru import logger


class TriangleChecker:
    def __init__(self, a, b, c):
        logger.info(f'Вызов __init__ у класса {self.__class__.__name__}')
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        coords = [self.a, self.b, self.c]
        if any(filter(lambda i: not isinstance(i, float | int) or i < 1, coords)):
            logger.info(f'Код = 1')
            return 1
        elif not all([(self.a + self.b) > self.c, (self.b + self.c) > self.a, (self.c + self.a) > self.b]):
            logger.info(f'Код = 2')
            return 2
        logger.info(f'Код = 3')
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())