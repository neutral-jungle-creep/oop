'''https://stepik.org/lesson/701976/step/10?unit=702077'''
from loguru import logger


class Factory:
    def build_sequence(self):
        logger.info(f'Вызов build_sequence у класса {self.__class__.__name__}')
        return []

    def build_number(self, string):
        logger.info(f'Вызов build_number у класса {self.__class__.__name__}')
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        logger.info(f'Вызов parse_format у класса {self.__class__.__name__}')
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
logger.info(f'res == {res}, type == {type(res)}')
